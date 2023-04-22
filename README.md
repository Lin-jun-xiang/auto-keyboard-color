<div>
    <img src="https://readme-typing-svg.demolab.com/?pause=1&size=50&color=e065b3&center=True&width=1200&height=120&vCenter=True&lines=點選+⭐+Star+給予+開發者+支持;任何問題+皆可於+Issue+討論!" />
</div>

## 自動化鍵盤背光設定

* 需求
    * `Python`
    * 鍵盤驅動軟體

* 詳細中文教學影片
    ![]
---

### 檔案說明及結構

* `color_grid_data.txt`: 紀錄您的鍵盤的每一個 RGB

* `keyboard_pos_data.txt`: 紀錄驅動軟體的 "鍵" 座標位置，視顯示器大小、驅動軟體改變，因此該資料一開始需要自己手動錄製

* `rgb_pos_data.txt`: 紀錄驅動軟體的 "RGB設定" 座標位置，視顯示器大小、驅動軟體改變，因此該資料一開始需要自己手動錄製

* `automator.py`: 負責有關 **"自動化"** 的程序

* `parse_image_color.py`: 負責解析圖片 RGB 的程序

* `config.py`: 設置檔案，包含 **"錄製相關快捷鍵"、"輸入圖片檔"、"控制介面"**...等

* `main.py`: 主要執行程式


```
.
├─ image/
│
├─ data
│  ├─ color_grid_data.txt
│  ├─ keyboard_pos_data.txt
|  ├─ rgb_pos_data.txt
|
├─ main.py
|
├─ config.py
|
├─ automator.py
|
├─ parse_image_color.py

```

---

### 重要提醒

* **鼠標快速移到螢幕左上角，可強制終止程序執行**

* **初次**使用該程序，須**先進行鼠標座標錄製**，紀錄 `/data/keyboard_pos_date.txt`、`/data/rgb_pos_data.txt`

---

### 功能
* 將圖片檔案離散成 RGB 像素
* 將像素自動化設定至鍵盤背光
* 自動清除鍵盤背光 (初始化)

---

### 方法

1. 獲取驅動軟體視窗
    ```python
    # 確認驅動軟體視窗名稱
    def get_all_windows() -> None:
        import pyautogui

        windows = pyautogui.getAllWindows()
        for window in windows:
            print(f'{window.title}')
    ```

2. 定義 `config.py`
    ```python
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
    ```

3. 執行 `main.py`，並先記錄鼠標座標

    * `[Automated]Already Have Positions Data ? (y/n)`: 選擇 `n`，並開始進行錄製
    * 參考 `config.py` 監聽按鍵及影片教學

4. 清除當前鍵盤背光 (初始化)

    * `[Automated]Do u want to cleanup color first ? (y/n)`: 選擇 `y` 清除

5. 進行自動設定背光

    * `[Automated]Do u want to setup keyboard color ? (y/n)`: 選擇 `y` 設定

---

### 鼠標追蹤測試
```python
import pyautogui

pyautogui.displayMousePosition()
```

---

### 範例 (新盟x75)

##### 自動化設定 RGB

輸入 `image.png/jpg`，將 RGB 解析並設定在驅動軟體上

   ![RGB_setup](https://github.com/Lin-jun-xiang/automate-keyboard-color/blob/main/demo_video/automator_setup.gif?raw=true)

##### 自動化清除 RGB (初始化)

   ![RGB_cleanup](https://github.com/Lin-jun-xiang/automate-keyboard-color/blob/main/demo_video/automator_cleanup.gif?raw=true)

##### 成果

    ![]



