import pyautogui as py
import keyboard
from time import sleep

from engine.draw import *
from maths import Vector2

from engine.objects.cube import Cube

py.PAUSE = 0.001

screenSize = Vector2(*py.size())
fov        = 20

cube = Cube()
renderRunning = True

py.hotkey("alt", "tab")
sleep(.2)

py.press("p")

while renderRunning:
    if keyboard.is_pressed('q'):
        renderRunning = False

    py.hotkey('ctrl', 'shift', 'del')
    py.hotkey('ctrl', 'shift', 'n')

    cube.render()
    cube.angle += 0.13

    sleep(.15)