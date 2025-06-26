# ----- ----- ----- -----
# line_detector.py
# Do not distribute or modify
# Author: DragonTaki (https://github.com/DragonTaki)
# Create Date: 2025/06/26
# Update Date: 2025/06/26
# Version: v1.0
# ----- ----- ----- -----

import cv2
import numpy as np
from typing import List, Tuple

def detect_grid_lines(binary_image: np.ndarray, min_line_gap: int = 10, min_black_ratio: float = 0.5) -> Tuple[List[int], List[int]]:
    """
    Detects horizontal and vertical grid lines in a binary (thresholded) image.

    Parameters:
        binary_image (np.ndarray): Binary image where grid lines are black (0) and background is white (255).
        min_line_gap (int): Minimum pixel gap to distinguish separate lines.
        min_black_ratio (float): Minimum ratio of black pixels in a row/column to consider it a grid line.

    Returns:
        (row_lines, col_lines):
            row_lines (List[int]): y-coordinates of horizontal lines
            col_lines (List[int]): x-coordinates of vertical lines
    """
    h, w = binary_image.shape

    # 1. Horizontal projection: horizontal line
    horizontal_projection = np.sum(binary_image == 0, axis=1)
    horizontal_mask = horizontal_projection > (min_black_ratio * w)
    row_lines = _extract_line_positions(horizontal_mask, min_line_gap)

    # 2. Vertical projection: vertical line
    vertical_projection = np.sum(binary_image == 0, axis=0)
    vertical_mask = vertical_projection > (min_black_ratio * h)
    col_lines = _extract_line_positions(vertical_mask, min_line_gap)

    return row_lines, col_lines

def _extract_line_positions(mask: np.ndarray, min_gap: int) -> List[int]:
    """
    Helper to extract line positions from a boolean mask.

    Parameters:
        mask (np.ndarray): 1D boolean array indicating presence of lines.
        min_gap (int): Minimum pixel gap to separate lines.

    Returns:
        List[int]: list of averaged line positions
    """
    positions = []
    current = []

    for i, val in enumerate(mask):
        if val:
            current.append(i)
        elif current:
            if len(current) > 1:
                positions.append(int(np.mean(current)))
            else:
                positions.append(current[0])
            current = []

    if current:
        if len(current) > 1:
            positions.append(int(np.mean(current)))
        else:
            positions.append(current[0])

    # Remove too-close positions
    filtered = []
    for pos in positions:
        if not filtered or abs(pos - filtered[-1]) >= min_gap:
            filtered.append(pos)

    return filtered
