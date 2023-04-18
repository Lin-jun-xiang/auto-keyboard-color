import numpy as np
from PIL import Image
import math

def get_color_grid(image_file: str, rgb_num: int, grid):
    """
    將圖像分配到網格中，並計算每個網格的平均色調。

    Args:
        image_file (str): 圖像檔案的路徑。
        rgb_num (int): 主要 RGB 成分之數量 
        grid (List[List[float]]): 一個包含布林值的二維矩陣，用於指定哪些網格應該被分配圖像色調。

    Returns:
        np.ndarray: 一個包含結果的二維 numpy 矩陣。每個元素都是一個包含 RGB 顏色值的字符串。

    Raises:
        TypeError: 如果 image_file 不是 str 型態或 grid 不是 List[List[bool]] 型態。

    """

    # 讀取圖片檔，將它轉換為 PIL.Image.Image 對象
    image = Image.open(image_file)

    # 計算網格的行和列
    num_rows = len(grid)
    num_cols = max(len(row) for row in grid)

    # 調整圖像大小為網格大小
    image = image.resize((int(num_cols), int(num_rows)))

    # 建立一個新的矩陣來存儲結果
    result = np.empty((num_rows, num_cols), dtype=object)
    result_str = np.empty((num_rows, num_cols), dtype=object)

    # 取得最大成分的前 n 個 RGB 值
    principal_rgb = get_rgb_component(image_file) if rgb_num == -1 else get_rgb_component(image_file)[:rgb_num]

    for row in range(num_rows):
        for col in range(len(grid[row])):
            if grid[row][col]:
                # 取得像素的顏色
                color = tuple(image.getpixel((col, row)))

                color = get_nearest_rgb(color, principal_rgb)

                # 存儲色調到結果矩陣中
                result[row][col] = color[0], color[1], color[2]
                result_str[row][col] = "rgb({},{},{})".format(color[0], color[1], color[2])

    np.savetxt('./data/color_grid_data.txt', result_str, delimiter=' ', fmt='%s')

    return result

def get_rgb_component(image_file):
    image = Image.open(image_file)

    # 取得圖片大小
    width, height = image.size

    # 儲存 RGB 值的字典，以及像素數量
    colors = {}
    pixel_count = width * height

    # 迭代所有像素，計算 RGB 值的出現次數
    for x in range(width):
        for y in range(height):
            r, g, b, _ = image.getpixel((x, y))
            color = (r, g, b)
            if color not in colors:
                colors[color] = 0
            colors[color] += 1

    # 計算 RGB 值的比例
    color_ratios = []
    for color, count in colors.items():
        ratio = count / pixel_count
        color_ratios.append((color, ratio))

    # 依照比例排序，由高到低
    color_ratios = sorted(color_ratios, key=lambda x: x[1], reverse=True)

    return color_ratios

def get_nearest_rgb(rgb, rgbs):
    best_match_color = None
    min_distance = float('inf')
    
    for color, _ in rgbs:
        distance = math.sqrt((rgb[0] - color[0]) ** 2 + (rgb[1] - color[1]) ** 2 + (rgb[2] - color[2]) ** 2)
        if distance < min_distance:
            min_distance = distance
            best_match_color = color
            
    return best_match_color



