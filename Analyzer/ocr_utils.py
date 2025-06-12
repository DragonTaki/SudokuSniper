# ----- ----- ----- -----
# ocr_utils.py
# Do not distribute or modify
# Author: DragonTaki (https://github.com/DragonTaki)
# Create Date: 2025/06/12
# Update Date: 2025/06/12
# Version: v1.0
# ----- ----- ----- -----

import pytesseract
import cv2

def recognize_digits(grid_image):
    # 分割為 9x9 格子
    h, w = grid_image.shape[:2]
    cell_h, cell_w = h // 9, w // 9
    board = []

    for i in range(9):
        row = []
        for j in range(9):
            cell = grid_image[i*cell_h:(i+1)*cell_h, j*cell_w:(j+1)*cell_w]
            digit = extract_digit(cell)
            row.append(digit)
        board.append(row)
    return board

def extract_digit(cell_img):
    gray = cv2.cvtColor(cell_img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)
    cnts, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(cnts) == 0:
        return 0

    # 使用 pytesseract 辨識
    text = pytesseract.image_to_string(gray, config='--psm 10 digits')
    try:
        return int(text.strip())
    except:
        return 0
