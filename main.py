import keyboard
import time
import pyautogui

isClicking = False


def set_clicker():
    global isClicking
    if isClicking:
        isClicking = False
        pyautogui.mouseUp()
        print('Макрос выключен')
    else:
        isClicking = True
        pyautogui.mouseDown()
        print('Макрос включен')


keyboard.add_hotkey('shift + z', set_clicker)

while True:
    if isClicking:
        for a in range(1, 1):
            a += 1
            time.sleep(1000)
            #550 - алм. кирка
            #1200 - алм. эф4, пр3
            keyboard.send(str(a))
