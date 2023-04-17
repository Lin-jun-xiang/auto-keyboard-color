from config import IMG_PATH
import json
import numpy as np
from PIL import Image

with open('./potsition_data/keyboard_data.txt', 'r') as file:
    keyboard_positions = json.load(file)

grid = keyboard_positions
image_file = './image/2.png'
img_scale = 1

# 讀取圖片檔，將它轉換為 PIL.Image.Image 對象
image = Image.open(image_file)

# 計算網格的行和列
num_rows = len(grid)
num_cols = max(len(row) for row in grid)

# 計算每個網格的大小
grid_width = image.width / num_cols
grid_height = image.height / num_rows

# 調整圖像大小為網格大小
image = image.resize((int(num_cols * grid_width * img_scale), int(num_rows * grid_height * img_scale)))

# 將圖像轉換為numpy array
image_array = np.array(image)

# 建立一個新的矩陣來存儲結果
result = np.empty((num_rows, num_cols), dtype=object)

for row in range(num_rows):
    for col in range(len(grid[row])):
        if grid[row][col]:
            # 計算網格中心點的位置
            center_x = int((col + 0.5) * grid_width)
            center_y = int((row + 0.5) * grid_height)

            # 取得中心像素的顏色
            avg_color = tuple(image.getpixel((center_x, center_y)))

            # 存儲色調到結果矩陣中
            result[row][col] = "rgb({},{},{})".format(avg_color[0], avg_color[1], avg_color[2])

np.savetxt('./data/color_grid_data.txt', result, delimiter=' ', fmt='%s')


