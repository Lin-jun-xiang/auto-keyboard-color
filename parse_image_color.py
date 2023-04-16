import numpy as np
from PIL import Image

def get_color_grid(image_file, grid):
    """
    將圖像分配到網格中，並計算每個網格的平均色調。

    Args:
        image_file (str): 圖像檔案的路徑。
        grid (List[List[bool]]): 一個包含布林值的二維矩陣，用於指定哪些網格應該被分配圖像色調。

    Returns:
        np.ndarray: 一個包含結果的二維 numpy 矩陣。每個元素都是一個包含 RGB 顏色值的字符串。

    Raises:
        TypeError: 如果 image_file 不是 str 型態或 grid 不是 List[List[bool]] 型態。

    Example:
        image_file = "example.jpg"
        grid = [[True, False, True], [False, True, False]]
        result = assign_image_to_grid(image_file, grid)
    """

    # 讀取圖片檔，將它轉換為 PIL.Image.Image 對象
    image = Image.open(image_file)

    # 計算網格的行和列
    num_rows = len(grid)
    num_cols = max(len(row) for row in grid)

    # 計算每個網格的大小
    grid_width = image.width / num_cols
    grid_height = image.height / num_rows

    # 調整圖像大小為網格大小
    image = image.resize((int(num_cols * grid_width), int(num_rows * grid_height)))

    # 將圖像轉換為numpy array
    image_array = np.array(image)

    # 建立一個新的矩陣來存儲結果
    result = np.empty((num_rows, num_cols), dtype=object)

    # 分配圖像色調到網格
    for row in range(num_rows):
        for col in range(len(grid[row])):
            if grid[row][col]:
                # 計算網格中心點的位置
                center_x = int((col + 0.5) * grid_width)
                center_y = int((row + 0.5) * grid_height)

                # 取得中心像素的顏色
                avg_color = tuple(image.getpixel((center_x, center_y)))

                # 存儲色調到結果矩陣中
                result[row][col] = (avg_color[0], avg_color[1], avg_color[2])
    return result