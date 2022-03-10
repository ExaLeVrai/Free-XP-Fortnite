eimport time
import pyautogui
import sys

x = pyautogui.confirm(text='Are you sure you would like to enter?', title='Warning', buttons=['OK', 'Cancel'])

if x == 'Cancel':
    sys.exit()

while True:
    pyautogui.press("q")
    time.sleep(1.8)