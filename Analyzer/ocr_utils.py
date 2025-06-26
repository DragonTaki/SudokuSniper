# ----- ----- ----- -----
# ocr_utils.py
# Do not distribute or modify
# Author: DragonTaki (https://github.com/DragonTaki)
# Create Date: 2025/06/12
# Update Date: 2025/06/26
# Version: v1.1
# ----- ----- ----- -----

import pytesseract
import cv2
from pathlib import Path

tesseract_path = (
    Path(__file__).resolve().parent.parent / "Third-Party" / "Tesseract" / "tesseract.exe"
)
pytesseract.pytesseract.tesseract_cmd = str(tesseract_path)

def recognize_digits_from_files(cell_paths_2d):
    board = []

    for row_paths in cell_paths_2d:
        row_digits = []
        for cell_path in row_paths:
            digit = extract_digit_from_file(cell_path)
            row_digits.append(digit)
        board.append(row_digits)

    return board

def extract_digit_from_file(image_path):
    img = cv2.imread(image_path)
    if img is None:
        return 0

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)
    cnts, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(cnts) == 0:
        return 0

    text = pytesseract.image_to_string(gray, config='--psm 10 digits')
    try:
        return int(text.strip())
    except:
        return 0
