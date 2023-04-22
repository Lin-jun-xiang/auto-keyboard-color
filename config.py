# 定义监听的按键
KEY_TO_RECORD = 'space' # 每次按下 space 即記錄當前鼠標座標
KEY_TO_STOP = 'ctrl+c' # 按下 ctrl+c 即暫停當前錄製
KEY_TO_SPLIT = 's'  # 按下 s 即提示程序分段

# 定義輸入圖片路徑
IMG_PATH = './image/四色.png'

# 定義 RGB value 數量
# 例如一張圖片60%紅色、30%藍色、10%白色，RGB_NUM=2，就萃取最大成分的紅、藍 (RGB_NUM=-1，全取)
RGB_NUM = -1

# 定義目標視窗 Title
WINDOW_TITLE = 'X75 RGB Keyboard'

# 定義詢問與執行自動化的時間區間
TIME_LATENCY = 3
