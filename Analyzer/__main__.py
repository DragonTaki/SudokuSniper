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

sys.path.insert(0, os.path.dirname(__file__))
from analyzer import analyze_image

def main():
    if len(sys.argv) != 2:
        print(json.dumps({"error": "Image path not provided"}))
        return

    image_path = sys.argv[1]
    try:
        result = analyze_image(image_path)
        print(json.dumps(result))
    except Exception as e:
        print(json.dumps({"error": str(e)}))

if __name__ == "__main__":
    main()
