# ----- ----- ----- -----
# grid_finder.py
# Do not distribute or modify
# Author: DragonTaki (https://github.com/DragonTaki)
# Create Date: 2025/06/12
# Update Date: 2025/06/26
# Version: v1.1
# ----- ----- ----- -----

import cv2
import numpy as np
import os
from debug_utils import save_debug_image

def find_sudoku_grid(thresh_image, original_image=None, debug_dir=None):
    """輸入二值化圖，找出最大的四邊形輪廓並裁切"""
    print(f"[DEBUG] Starting find_sudoku_grid. Debug dir: {debug_dir}")
    edges = cv2.Canny(thresh_image, 50, 150)

    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < 1000:
            continue

        # 嘗試使用四點擬合
        approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)
        if len(approx) == 4:
            pts = approx.reshape(4, 2)
            source_image = original_image if original_image is not None else thresh_image
            warped = four_point_transform(source_image, order_points(pts))
            if debug_dir:
                debug_img = cv2.cvtColor(thresh_image.copy(), cv2.COLOR_GRAY2BGR)
                cv2.drawContours(debug_img, [approx], -1, (0, 255, 0), 2)
                save_debug_image(debug_dir, "03b-approx-corners", debug_img)
            return warped

    # fallback: 使用 minAreaRect 擬合旋轉矩形
    for cnt in contours:
        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)
        box = np.intp(box)
        source_image = original_image if original_image is not None else thresh_image
        warped = four_point_transform(source_image, order_points(pts))
        if debug_dir:
            debug_img = cv2.cvtColor(thresh_image.copy(), cv2.COLOR_GRAY2BGR)
            cv2.drawContours(debug_img, [box], -1, (0, 0, 255), 2)
            save_debug_image(debug_dir, "03c-rotated-rect", debug_img)
        return warped

    return None


def order_points(pts):
    """將四點依序排列為 [top-left, top-right, bottom-right, bottom-left]"""
    rect = np.zeros((4, 2), dtype="float32")

    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]  # top-left
    rect[2] = pts[np.argmax(s)]  # bottom-right

    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]  # top-right
    rect[3] = pts[np.argmax(diff)]  # bottom-left

    return rect

def four_point_transform(image, pts):
    rect = order_points(pts)
    (tl, tr, br, bl) = rect

    # 計算轉換後圖像的寬與高
    widthA = np.linalg.norm(br - bl)
    widthB = np.linalg.norm(tr - tl)
    maxWidth = int(max(widthA, widthB))

    heightA = np.linalg.norm(tr - br)
    heightB = np.linalg.norm(tl - bl)
    maxHeight = int(max(heightA, heightB))

    # 定義變換後的目標點
    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]
    ], dtype="float32")

    # 建立透視轉換矩陣並應用
    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

    return warped
