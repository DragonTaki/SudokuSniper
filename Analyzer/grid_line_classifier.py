# ----- ----- ----- -----
# grid_line_classifier.py
# Do not distribute or modify
# Author: DragonTaki (https://github.com/DragonTaki)
# Create Date: 2025/06/26
# Update Date: 2025/06/26
# Version: v1.0
# ----- ----- ----- -----

import numpy as np
import cv2
from grid_constants import GridLine

def classify_grid_lines(row_lines, col_lines, binary_image):
    """
    分析格線的位置與類型（細線、粗線、邊界）

    Parameters:
        row_lines (List[int]): 所有水平線的像素 Y 座標
        col_lines (List[int]): 所有垂直線的像素 X 座標
        binary_image (np.ndarray): 二值化影像（黑白）

    Returns:
        Tuple[List[GridLine], List[GridLine]]: 橫線類型、豎線類型
    """
    row_types = []
    col_types = []

    # 偵測水平方向格線類型
    for i, y in enumerate(row_lines):
        if y < 0 or y >= binary_image.shape[0]:
            row_types.append(GridLine.INVALID)
            continue

        # 取橫線附近的一條橫帶
        band = binary_image[max(0, y - 2):min(binary_image.shape[0], y + 3), :]
        black_ratio = np.mean(band == 0)

        if black_ratio > 0.5:
            if i == 0 or i == len(row_lines) - 1:
                row_types.append(GridLine.BORDER)
            elif black_ratio > 0.9:
                row_types.append(GridLine.THICK)
            else:
                row_types.append(GridLine.THIN)
        else:
            row_types.append(GridLine.NONE)

    # 偵測垂直方向格線類型
    for j, x in enumerate(col_lines):
        if x < 0 or x >= binary_image.shape[1]:
            col_types.append(GridLine.INVALID)
            continue

        band = binary_image[:, max(0, x - 2):min(binary_image.shape[1], x + 3)]
        black_ratio = np.mean(band == 0)

        if black_ratio > 0.5:
            if j == 0 or j == len(col_lines) - 1:
                col_types.append(GridLine.BORDER)
            elif black_ratio > 0.9:
                col_types.append(GridLine.THICK)
            else:
                col_types.append(GridLine.THIN)
        else:
            col_types.append(GridLine.NONE)

    return row_types, col_types
