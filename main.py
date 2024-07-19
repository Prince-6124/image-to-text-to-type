import pyautogui
import time
from PIL import Image
from pytesseract import pytesseract



def type_message():
    # time.sleep(10)

    for line in open("to-type.txt", "r"):
        pyautogui.typewrite(line)


    