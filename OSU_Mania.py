"""import pynput
import pyautogui
#from pynput import mouse, keyboard
from pynput.keyboard import Key, Controller
import time
#from pynput.mouse import Controller


keyboard = Controller()
var = 1


while True:
    var = input("type 0 when ready: ")
    if var == var:
        print("20 sec")
        time.sleep(5)
        print("15 sec")
        time.sleep(5)
        print("10 sec")
        time.sleep(5)
        print("5 sec")
        time.sleep(5)
        print("start")
        time.sleep(1)
        while True:
            #print(pyautogui.position())

            x,y = pyautogui.position()

            if (x,y) != (4200, 460):
                pynput.mouse.Controller().position = (4200, 460)

            if x > 4200 and x <4250 and y >660:
                keyboard.press(Key.space)
                #time.sleep(0.001)
                keyboard.release(Key.space)
                print("1")

            if (x,y) != (4200, 460):
                pynput.mouse.Controller().position = (4200, 460)

            if x > 4250 and x <4300 and y >660:
                keyboard.press('s')
                #time.sleep(0.001)
                keyboard.release('s')
                print("2")

            #if (x,y) != (4200, 460):
                #pynput.mouse.Controller().position = (4200, 460)

            if x > 4350 and x <4400 and y >660:
                keyboard.press('d')
                #time.sleep(0.001)
                keyboard.release('d')
                print("3")

            #if (x,y) != (4200, 460):
                #pynput.mouse.Controller().position = (4200, 460)

            if x > 4400 and x <4470 and y >660:
                keyboard.press('f')
                #time.sleep(0.001)
                keyboard.release('f')
                print("4")

            if (x,y) == (0,0):
                break"""

import serial
from pynput.keyboard import Key, Controller
import time

ser = serial.Serial('COM3', 115200)
keyboard = Controller()

print(ser.name)
time.sleep(2)
print("start")

cheack_1 = 0
cheack_2 = 0
cheack_3 = 0
cheack_4 = 0
help_=[0,0,0,0]
old=[0,0,0,0]
count = 1

def spam_old(count,button):
    if count == 1:
        old[0] = button
    elif count == 2:
        old[1] = button
    elif count == 3:
        old[2] = button
    else:
        old[3] = button


def spam(count, button, old):
    if count == 1:
        help_[0] = button
    elif count == 2:
        help_[1] = button
    elif count == 3:
        help_[2] = button
    else:
        help_[3] = button
    if count == 4:
        count = 0

    if old != help_[count]:
        return help_[count]
    else:
        return 0


while True:
    r = ser.read()
    try:
        # print(int(r))
        button = int(r)

        count += 1
        #button = spam(count, button, old)
        #spam_old(count,button)
        #print(count,"hi")

        if button == 1:
            if cheack_1 == 0:
                print("1_on")
                keyboard.press('k')
                cheack_1 = 1

        if button == 2:
            # print("1")
            keyboard.release('k')
            cheack_1 = 0

        if button == 3:
            if cheack_2 == 0:
                print("2_on")
                keyboard.press('j')
                cheack_2 = 1

        if button == 4:
            # print("2")
            keyboard.release('j')
            cheack_2 = 0

        if button == 5:
            if cheack_3 == 0:
                print("3_on")
                keyboard.press('f')
                cheack_3 = 1

        if button == 6:
            # print("3")
            keyboard.release('f')
            cheack_3 = 0

        if button == 7:
            if cheack_4 == 0:
                print("4_on")
                keyboard.press('d')
                cheack_4 = 1

        if button == 8:
            # print("4")
            keyboard.release('d')
            cheack_4 = 0
    except:
        print()
        #
