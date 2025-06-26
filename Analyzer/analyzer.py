# ----- ----- ----- -----
# analyzer.py
# Do not distribute or modify
# Author: DragonTaki (https://github.com/DragonTaki)
# Create Date: 2025/06/12
# Update Date: 2025/06/26
# Version: v1.1
# ----- ----- ----- -----

import cv2
import os

from cell_extractor import extract_cells
from debug_utils import save_debug_image
from grid_finder import find_sudoku_grid
from preprocess import preprocess_image
from ocr_utils import recognize_digits_from_files

def analyze_image(image_path: str, debug_dir: str = None) -> dict:
    image = cv2.imread(image_path)

    if image is None:
        raise ValueError("Cannot open image.")
    
    if debug_dir:
        save_debug_image(debug_dir, "01-original", image)

    gray, thresh = preprocess_image(image)

    if debug_dir:
        save_debug_image(debug_dir, "02-gray", gray)
        save_debug_image(debug_dir, "03-threshold", thresh)

    grid = find_sudoku_grid(thresh, image, debug_dir=debug_dir)
    if grid is None:
        raise ValueError("Failed to detect Sudoku grid.")
    
    if debug_dir:
        save_debug_image(debug_dir, "04-grid", grid)

    cell_dir = os.path.join(debug_dir, "cells")
    cell_paths = extract_cells(grid, cell_dir)
    digits = recognize_digits_from_files(cell_paths)
    
    is_valid = (
        isinstance(digits, list) and
        len(digits) == 9 and
        all(isinstance(r, list) and len(r) == 9 for r in digits)
    )

    return {
        "board": digits,
        "type": "standard" if is_valid else "unknown"
    }
