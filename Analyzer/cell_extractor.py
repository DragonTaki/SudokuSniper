# ----- ----- ----- -----
# cell_extractor.py
# Do not distribute or modify
# Author: DragonTaki (https://github.com/DragonTaki)
# Create Date: 2025/06/26
# Update Date: 2025/06/26
# Version: v1.0
# ----- ----- ----- -----

import os
import cv2
import numpy as np
from pathlib import Path

def extract_cells(grid_image, save_dir):
    """
    Splits a grid image into NxM cells based on detected grid lines.
    Returns a 2D list of file paths representing each cell.
    """
    os.makedirs(save_dir, exist_ok=True)

    # Detect grid lines
    verticals, horizontals = detect_grid_lines(grid_image)
    verticals = sorted(set(verticals))
    horizontals = sorted(set(horizontals))

    cell_paths = []
    for i in range(len(horizontals) - 1):
        row_paths = []
        for j in range(len(verticals) - 1):
            y1, y2 = horizontals[i], horizontals[i + 1]
            x1, x2 = verticals[j], verticals[j + 1]
            cell = grid_image[y1:y2, x1:x2]
            filename = f"cell_{i+1}-{j+1}.png"
            full_path = os.path.join(save_dir, filename)
            cv2.imwrite(full_path, cell)
            row_paths.append(full_path)
        cell_paths.append(row_paths)

    return cell_paths

def detect_grid_lines(image):
    """
    Detects horizontal and vertical lines in the image.
    Returns two lists: vertical line x-positions, horizontal line y-positions.
    Also tracks thickness to distinguish bold lines (region separators).
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) if len(image.shape) == 3 else image
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=150, minLineLength=40, maxLineGap=5)
    if lines is None:
        return [], []

    verticals = []
    horizontals = []
    for line in lines:
        x1, y1, x2, y2 = line[0]
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)

        if dx < 10 and dy > 20:  # vertical line
            verticals.append((x1 + x2) // 2)
        elif dy < 10 and dx > 20:  # horizontal line
            horizontals.append((y1 + y2) // 2)

    return verticals, horizontals
