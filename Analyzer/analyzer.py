# ----- ----- ----- -----
# analyzer.py
# Do not distribute or modify
# Author: DragonTaki (https://github.com/DragonTaki)
# Create Date: 2025/06/12
# Update Date: 2025/06/12
# Version: v1.0
# ----- ----- ----- -----

import cv2
from ocr_utils import recognize_digits
from grid_finder import find_sudoku_grid

def analyze_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Cannot open image.")

    grid = find_sudoku_grid(image)
    if grid is None:
        raise ValueError("Failed to detect Sudoku grid.")

    digits = recognize_digits(grid)
    return {
        "board": digits,
        "type": "standard" if len(digits) == 9 and all(len(r) == 9 for r in digits) else "unknown"
    }
