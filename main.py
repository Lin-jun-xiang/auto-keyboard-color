from automator import get_positions, set_keyboard_colors, clean_up_color
from parse_image_color import get_color_grid
from config import IMG_PATH
import winsound
import json

while True:
    positions_file = input("Already Have Positions Data ? (y/n)")

    if positions_file.lower() == 'y':
        # 從文本文件中讀取 JSON 數據
        with open('./potsition_data/keyboard_data.txt', 'r') as file:
            keyboard_positions = json.load(file)

        with open('./potsition_data/RGB_data.txt', 'r') as file:
            rgb_positions = json.load(file)

        break

    if positions_file.lower() == 'n':
        # 取得驅動軟體上的座標
        keyboard_positions = get_positions('keyboard')

        with open('./potsition_data/keyboard_data.txt', 'w') as file:
            json.dump(keyboard_positions, file)

        # 取得驅動軟體上的 RGB設置 座標
        rgb_positions = get_positions('RGB setting')

        with open('./potsition_data/rgb_data.txt', 'w') as file:
            json.dump(rgb_positions, file)

        break

rgb_values_grid = get_color_grid(IMG_PATH, keyboard_positions)

cleanup = input('Do u want to cleanup color first ? (y/n)')
if cleanup.lower() == 'y':
    clean_up_color(keyboard_positions)

print(rgb_values_grid)
set_keyboard_colors(keyboard_positions, rgb_positions, rgb_values_grid)

winsound.PlaySound('exclamation', winsound.SND_ALIAS)
