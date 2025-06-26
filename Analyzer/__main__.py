# ----- ----- ----- -----
# __main__.py
# Do not distribute or modify
# Author: DragonTaki (https://github.com/DragonTaki)
# Create Date: 2025/06/05
# Update Date: 2025/06/05
# Version: v1.0
# ----- ----- ----- -----

import os
import sys
import json
from pathlib import Path

sys.path.insert(0, os.path.dirname(__file__))
from analyzer import analyze_image
from debug_utils import create_debug_folder

def main():
    if len(sys.argv) != 2:
        print(json.dumps({"error": "Image path not provided"}))
        return

    image_path = sys.argv[1]
    base_debug_dir = (Path(__file__).resolve().parent.parent / "Temp")
    debug_dir = create_debug_folder(base_debug_dir)

    try:
        result = analyze_image(image_path, debug_dir=debug_dir)
        result["debug_folder"] = os.path.abspath(debug_dir)
        print(json.dumps(result))
    except Exception as e:
        print(json.dumps({"error": str(e)}))

if __name__ == "__main__":
    test_image_path = (Path(__file__).resolve().parent.parent / "Temp" / "capture.png")
    sys.argv = [sys.argv[0], test_image_path]
    main()
