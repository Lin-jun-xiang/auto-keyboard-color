from config import IMG_PATH
import json
import numpy as np
from PIL import Image, ImageDraw

with open('./data/keyboard_pos_data.txt', 'r') as file:
    keyboard_positions = json.load(file)

grid = keyboard_positions
image_file = './image/4.png'

# 讀取圖片檔，將它轉換為 PIL.Image.Image 對象
image = Image.open(image_file)

# 計算網格的行和列
num_rows = len(grid)
num_cols = max(len(row) for row in grid)

# 計算每個網格的大小
grid_width = image.width / num_cols
grid_height = image.height / num_rows

# 調整圖像大小為網格大小
image = image.resize((int(num_cols), int(num_rows)))

# 建立一個新的矩陣來存儲結果
result = np.empty((num_rows, num_cols), dtype=object)

for row in range(num_rows):
    for col in range(len(grid[row])):
        if grid[row][col]:
            # 取得像素的顏色
            color = tuple(image.getpixel((col, row)))

            # 存儲色調到結果矩陣中
            result[row][col] = "rgb({},{},{})".format(color[0], color[1], color[2])

np.savetxt('./data/color_grid_data.txt', result, delimiter=' ', fmt='%s')


image_file = './image/螢幕擷取畫面 2023-04-17 192044.png'

# 讀取圖片檔，將它轉換為 PIL.Image.Image 對象
image = Image.open(image_file)
[i * 2 for i in image.size]
image = image.resize((1800, 1300))
image.save('./image/t.png')