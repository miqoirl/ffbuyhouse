from pyautogui import *
import pyautogui
import random
import time
import configparser

# Config
config = configparser.ConfigParser()
config.read('config.ini')

confirm_button = config['Settings']['ConfirmButton']
images_path = 'images/'
CONFIDENCE = 0.95
fail_count = 0

def click(x_loc,y_loc):
    pyautogui.click(clicks=2, interval=0.25, x=x_loc, y=y_loc)

def find_button(path):
    button_pos = pyautogui.locateOnScreen(images_path + path, confidence=CONFIDENCE)
    button = pyautogui.center(button_pos)
    return button

pyautogui.keyDown('alt')
time.sleep(.2)
pyautogui.press('tab')
time.sleep(.2)
pyautogui.keyUp('alt')

while fail_count < 3:
    pyautogui.press(confirm_button)
    # click center of screen
    for i in range(4):
        pyautogui.press(confirm_button)
        time.sleep(round(random.uniform(0.4,0.6), 2))

    try:
        yes_button_loc = find_button('yes_button.png')
        click(yes_button_loc[0], yes_button_loc[1])
        fail_count = 0
    except TypeError: # button not found on screen
        fail_count += 1
        t = time.localtime()
        print('[{}] Fail count: {}'.format(time.strftime("%H:%M:%S", t), fail_count))

    time.sleep(random.uniform(0.5,1))

# Fail count > 3
pyautogui.press('esc')
# Move backwards
pyautogui.keyDown('s')
time.sleep(2)
pyautogui.keyUp('s');

t = time.localtime()
print('[{}] Fail count exceeded, exiting.'.format(time.strftime("%H:%M:%S", t)))