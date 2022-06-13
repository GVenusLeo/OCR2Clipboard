<h1 align="center">QuickOCR</h1>

## 功能

截图并自动识别文字，识别结果保存在系统粘贴板中。

## 使用

1. 克隆到本地后在根目录中执行：

```powershell
pipenv install
pipenv run python QuickOCR.py
```

2. 截图并识别：将鼠标移动到待识别图片的一角，按下 `Alt+Z` 后，移动鼠标到对角线的另一角，再次按下 `Alt+Z` 即可。

3. 等待识别完成后，结果会自动写入系统剪切板。

# 说明

OCR 识别基于 [EasyOCR](https://github.com/jaidedai/easyocr) 实现。
