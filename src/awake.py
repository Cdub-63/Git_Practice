import pyautogui
import time
import sys
from datetime import datetime
pyautogui.FAILSAFE = False
numMin = None
if ((len(sys.argv)<2) or sys.argv[1].isalpha() or int(sys.argv[1])<1):
    numMin = 3
else:
    numMin = int(sys.argv[1])
while(True):
    x=0
    mouse_pos = pyautogui.position()
    while(x<numMin):
        mouse_pos2 = pyautogui.position()
        if mouse_pos != mouse_pos2:
            x = 0
        else:
            time.sleep(60)
            x+=1
    for i in range(0,200):
        pyautogui.moveTo(0,i*4)
    pyautogui.moveTo(1,1)
    for i in range(0,3):
        pyautogui.press("shift")
    print("Movement made at {}".format(datetime.now().time()))
