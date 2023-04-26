import pyautogui
import pydirectinput
import time
import random
import math
import argparse
from datetime import date


def sleep(min, max):
    sleepTime = random.randint(min, max) / 1000.0
    if sleepTime < 0:
        return
    time.sleep(sleepTime)


sleep(2000, 2300)
# pydirectinput.press("`")



while True:
    print(pyautogui.displayMousePosition())
    i = input("Enter text (or Enter to quit): ")
    if not i:
        break
