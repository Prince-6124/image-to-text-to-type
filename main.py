import pyautogui
import time
from PIL import Image
from pytesseract import pytesseract

def extract_text():
    # Open the image
    image = Image.open('image.png')

    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    # Configure Tesseract (optional for better accuracy)
    config = '--oem 3 --psm 6'  # Improve text layout and digit recognition

    # Extract text from image
    text = pytesseract.image_to_string(image, config=config)

    with open('to-type.txt','w') as f:
        f.write(text)

def type_message():
    time.sleep(delay)
    for line in open("to-type.txt", "r"):
        line = line.split(' ')
        for word in line:
            pyautogui.typewrite(word)
            pyautogui.typewrite(' ')
            time.sleep(speed)

def main():
    # delay: float = input("Enter the Delay : ")
    # speed: float = input("Enter Desired Speed :")
    extract_text()
    type_message()

if __name__ == '__main__':
    main()