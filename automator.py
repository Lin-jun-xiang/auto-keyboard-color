import time
from functools import wraps
import keyboard
import pyautogui
from config import KEY_TO_RECORD, KEY_TO_SPLIT, KEY_TO_STOP, WINDOW_TITLE

def get_window(func):
    @wraps(func)
    def wrapper(*arg, **kwarg):
        try:
            # 將視窗設置為活動視窗
            window = pyautogui.getWindowsWithTitle(WINDOW_TITLE)[0]
            # window.activate()
            window.maximize()

            print(f'Listening {WINDOW_TITLE} now')
            time.sleep(2)

            value = func(*arg, **kwarg)
        except Exception as e:
            print(e)
        return value
    return wrapper

@get_window
def get_positions(record_target: str):
    # 获取屏幕大小
    screen_width, screen_height = pyautogui.size()

    # 定义记录位置的列表
    click_positions = []

    print(f'Press "{KEY_TO_RECORD}" to record {record_target}.\n',
          f'Press "{KEY_TO_SPLIT}" to split the record.\n',
          f'Press "{KEY_TO_STOP}" to stop record.')

    # 定义按键事件的处理函数
    def on_key_press(event):
        if event.name == KEY_TO_RECORD:
            # 如果用户按下要记录的键，记录鼠标位置
            x, y = pyautogui.position()
            # 将坐标转换为通用的坐标系
            x = x * 100 / screen_width
            y = y * 100 / screen_height
            click_positions.append((x, y))
        elif event.name == KEY_TO_SPLIT:
            # 如果用户按下分段键，记录特殊坐标 (-1, -1)
            print('Split...')
            click_positions.append((-1, -1))
        elif event.name == KEY_TO_STOP:
            # 如果用户按下停止键，停止监听
            raise KeyboardInterrupt

    # 注册按键事件监听器
    keyboard.on_press(on_key_press)

    # 开始监听键盘输入
    try:
        keyboard.wait(KEY_TO_STOP)
    except KeyboardInterrupt:
        # 如果用户按下停止键，停止监听并打印记录的位置
        pass

    # 返回所有记录的位置
    return split_positions(click_positions)

def split_positions(click_positions):
    split_indices = [i for i, pos in enumerate(click_positions) if pos == (-1, -1)]

    if not split_indices:
        return click_positions

    split_indices += [len(click_positions)-1]

    sub_positions = []
    for i in range(len(split_indices)):
        if i == 0:
            sub_positions.append(click_positions[:split_indices[i]])

        elif i == len(split_indices)-1:
            sub_positions.append(click_positions[split_indices[i-1]+1:split_indices[i]+1])
        
        else:
            sub_positions.append(click_positions[split_indices[i-1]+1:split_indices[i]])

    return sub_positions

@get_window
def set_keyboard_colors(keyboard_positions, rgb_positions, rgb_values_grid):
    """_summary_

    Args:
        keyboard_positions: 
        ```
            [
             [(), ()],
             [(), (), ()],
             [(), (), ()]
             ]
        ```
        rgb_positions:
        ```
            [
            (),
            (),
            ()
            ]
        ```
        rgb_values_grid:
        ```
            [
             [(), ()],
             [(), (), ()],
             [(), (), ()]
             ]
        ```
    """
    # 获取屏幕大小
    screen_width, screen_height = pyautogui.size()

    # 遍歷鍵盤座標、鍵盤座標對應的 rgb 值

    for row_i in range(len(keyboard_positions)):
        key_coords = keyboard_positions[row_i]
        rgbs = rgb_values_grid[row_i]

        for key_i in range(len(key_coords)):
            key_coord = key_coords[key_i]
            rgb = rgbs[key_i]

            if key_i == 0 or (key_i != 0 and rgb != rgbs[key_i - 1]):
                # 如果當前 rgb 與前一次 rgb 不一樣，再做設定
                # 使用 RGB設定座標 輸入 RGB 值
                for rgb_i in range(len(rgb_positions)):
                    pyautogui.click(
                        rgb_positions[rgb_i][0]*screen_width/100,
                        rgb_positions[rgb_i][1]*screen_height/100
                        )
                    pyautogui.press('right', presses=3)
                    pyautogui.press('backspace', presses=3)
                    pyautogui.typewrite(f"{int(rgb[rgb_i])}")

            # 點選鍵盤位置、賦予該鍵 RGB
            pyautogui.click(
                key_coord[0]*screen_width/100,
                key_coord[1]*screen_height/100
                )

@get_window
def clean_up_color(keyboard_positions):
    screen_width, screen_height = pyautogui.size()

    for row_i in range(len(keyboard_positions)):
        key_coords = keyboard_positions[row_i]

        for key_i in range(len(key_coords)):
            key_coord = key_coords[key_i]
            pyautogui.click(
                key_coord[0]*screen_width/100,
                key_coord[1]*screen_height/100
                )
