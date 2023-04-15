## 自動化鍵盤背光設定

* 需求
    * `Python`

---

### 重要

* **鼠標快速移到螢幕左上角，可強制終止程序執行**

### 功能
* 將圖片檔案離散成 RGB 像素
* 將像素自動化設定至鍵盤背光

### 方法

```python
# 確認驅動軟體視窗名稱
def get_all_windows() -> None:
    import pyautogui

    windows = pyautogui.getAllWindows()
    for window in windows:
        print(f'{window.title}')
```

### 體驗鼠標追蹤
```python
import pyautogui

pyautogui.displayMousePosition()
```