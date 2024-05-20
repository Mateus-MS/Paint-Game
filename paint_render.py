import pyautogui as py
import keyboard
from time import sleep

from engine.draw import *
from maths import Vector3
from maths import Vector2

from engine.objects.triangle import Triangle

py.PAUSE = 0.0001

screenSize = Vector2(*py.size())
fov        = 20

py.hotkey("alt", "tab")
sleep(.2)

points = [
    Vector3(-100,  100, 10),
    Vector3(-100, -100, 10),
    Vector3( 100, -100, 10)
]

test = Triangle(*points)
renderRunning = True

while renderRunning:

    if keyboard.is_pressed('q'):
        renderRunning = False

    py.press('p')

    test.render()
    test.angle += 0.1
    sleep(.1)

    py.hotkey('ctrl', 'a')
    py.press('del')