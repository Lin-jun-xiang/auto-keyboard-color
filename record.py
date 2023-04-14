import pyautogui
import keyboard

# 定义记录位置的列表
click_positions = []

# 定义监听的按键
KEY_TO_RECORD = "space"
KEY_TO_STOP = "esc"

# 定义按键事件的处理函数
def on_key_press(event):
    if event.name == KEY_TO_RECORD:
        # 如果用户按下要记录的键，记录鼠标位置
        click_positions.append(pyautogui.position())
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

# 打印所有记录的位置
print(click_positions)
