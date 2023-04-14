from PIL import Image

# 读取图像
image = Image.open('./image/船底座星雲.jpg')

# 定义網格大小
n, m = 6, 10

# 将图像分割成 nxm 个矩形，获取每个矩形的 RGB 值
pixels = list(image.getdata())
pixel_count = len(pixels)
grid_size = pixel_count / (n * m)
grid_colors = []

for i in range(n * m):
    start = int(i * grid_size)
    end = int((i + 1) * grid_size)
    grid = pixels[start:end]
    avg_color = tuple(int(sum(channel) / len(channel)) for channel in zip(*grid))
    grid_colors.append(avg_color)




# # 循环遍历每个矩形并点击相应的键盘颜色
# for i in range(n * m):
#     color = grid_colors[i]
#     # 设置键盘颜色
#     # ...

#     # 点击键盘
#     # ...

#     # 等待一段时间
#     # ...