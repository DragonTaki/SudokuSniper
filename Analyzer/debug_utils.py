# ----- ----- ----- -----
# debug_utils.py
# Do not distribute or modify
# Author: DragonTaki (https://github.com/DragonTaki)
# Create Date: 2025/06/26
# Update Date: 2025/06/26
# Version: v1.0
# ----- ----- ----- -----

import os
import cv2
import time
import shutil
import re


MAX_DEBUG_FOLDERS = 3
_TIMESTAMP_PATTERN = re.compile(r"^\d{8}_\d{6}$")


# Create a new debug folder (with timestamp)
def create_debug_folder(base_dir: str) -> str:
    """Create a folder named with timestamp under the base_dir."""
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    path = os.path.join(base_dir, timestamp)
    os.makedirs(path, exist_ok=True)

    cleanup_old_debug_folders(base_dir, max_folders=MAX_DEBUG_FOLDERS)

    return path

# Save picture in a unified format
def save_debug_image(folder: str, step: str, image, ext=".png"):
    """Save an image with a step name into the folder."""
    filename = f"{step}{ext}"
    cv2.imwrite(os.path.join(folder, filename), image)

def cleanup_old_debug_folders(base_dir: str, max_folders: int):
    """Keep only the newest N folders, delete the rest."""
    if not os.path.exists(base_dir):
        return

    folders = [
        os.path.join(base_dir, d)
        for d in os.listdir(base_dir)
        if os.path.isdir(os.path.join(base_dir, d)) and is_timestamped_folder(d)
    ]

    # 排序：新 → 舊（保留最新）
    folders.sort(reverse=True)

    for folder in folders[max_folders:]:
        try:
            shutil.rmtree(folder)
        except Exception as e:
            print(f"[Warn] Failed to delete folder {folder}: {e}")

def is_timestamped_folder(name: str) -> bool:
    """Return True if folder name matches timestamp format YYYYMMDD_HHMMSS"""
    return bool(_TIMESTAMP_PATTERN.match(name))
