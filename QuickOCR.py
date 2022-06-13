"""
@ Author: GVenusLeo
@ Create: 2022-02-23
@ Descriptions: 主程序
"""

import time

import easyocr
import keyboard
import pyperclip
from PIL import ImageGrab
from pyautogui import position


def capture():
    """
    截取图片, 以截取时间为文件名, 保存在 images 文件夹下
    :return: 图片路径 path
    """
    # 获取前后两次鼠标位置
    print("-"*20)
    print("等待截图...")
    keyboard.wait('alt+z')
    x1, y1 = position()
    print("正在截图...")
    keyboard.wait('alt+z')
    x2, y2 = position()
    # 获取当前时间
    time_now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    # 图片路径
    image_path = 'images/' + time_now + '.png'
    # 截取图片
    ImageGrab.grab().crop((x1, y1, x2, y2)).save(image_path)
    print("截图成功, 图片路径:", image_path, "正在识别...")
    return image_path


def ocr(img_path):
    """
    识别图片, 结果保存在剪切板
    :param img_path: 图片路径
    :return: None
    """
    # 识别图片
    reader = easyocr.Reader(['ch_sim', 'en'])
    result = reader.readtext(img_path, detail=0)
    # 识别结果处理
    result_text = "".join(result)
    pre_str = [" ", "\n", ",", ".", "?", "!", ";", "(", ")"]
    tag_str = ["", "", "，", "？", "！", "；", "（", "）"]
    for i in range(len(pre_str)-1):
        result_text = result_text.replace(pre_str[i], tag_str[i])
    # 将识别结果保存在剪切板
    pyperclip.copy(result_text)
    print("识别成功, 结果已保存到剪切板!!!")
    print(">>> ", result_text)


if __name__ == '__main__':
    while True:
        ocr(capture())
