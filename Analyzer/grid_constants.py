# ----- ----- ----- -----
# grid_constants.py
# Do not distribute or modify
# Author: DragonTaki (https://github.com/DragonTaki)
# Create Date: 2025/06/26
# Update Date: 2025/06/26
# Version: v1.0
# ----- ----- ----- -----

from enum import IntEnum

class GridLine(IntEnum):
    INVALID = -1   # 無效線（例如空白區域外的線）
    NONE = 0       # 無線（兩格之間都空白）
    THIN = 1       # 細線（一般格子之間）
    THICK = 2      # 粗線（區塊分隔線）
    BORDER = 3     # 外框邊界線

LINE_COLORS = {
    GridLine.THIN: (100, 100, 255),    # 細藍線
    GridLine.THICK: (0, 200, 0),       # 粗綠線
    GridLine.BORDER: (0, 0, 255),      # 紅線（外框）
}
