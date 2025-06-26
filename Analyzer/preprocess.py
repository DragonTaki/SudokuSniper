# ----- ----- ----- -----
# preprocess.py
# Do not distribute or modify
# Author: DragonTaki (https://github.com/DragonTaki)
# Create Date: 2025/06/26
# Update Date: 2025/06/26
# Version: v1.0
# ----- ----- ----- -----

import cv2

def to_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def to_threshold(gray_image):
    return cv2.adaptiveThreshold(
        gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 2
    )

def preprocess_image(image):
    gray = to_grayscale(image)
    thresh = to_threshold(gray)
    return gray, thresh
