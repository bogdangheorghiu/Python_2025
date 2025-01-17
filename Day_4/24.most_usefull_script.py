

# pip install pyautogui

import pyautogui
import time
import random



screen_width, screen_hight = pyautogui.size()
print("Width:", screen_width, "Hight", screen_hight)

while True:
    seconds = random.randint(1, 3)
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)
    x_random = random.randint(0, screen_width)
    y_random = random.randint(0, screen_hight)
    pyautogui.moveTo(x_random, y_random, duration=1)
