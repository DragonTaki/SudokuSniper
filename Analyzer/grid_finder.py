# ----- ----- ----- -----
# grid_finder.py
# Do not distribute or modify
# Author: DragonTaki (https://github.com/DragonTaki)
# Create Date: 2025/06/12
# Update Date: 2025/06/12
# Version: v1.0
# ----- ----- ----- -----

import cv2
import numpy as np

def find_sudoku_grid(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, 50, 150)

    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)
        if len(approx) == 4:
            return four_point_transform(image, approx.reshape(4, 2))

    return None

def four_point_transform(image, pts):
    # 略：可使用 OpenCV warpPerspective 實作四點轉換
    # 回傳裁剪後的數獨圖片
    pass
