import pyautogui as py
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
    Vector3( 100, -100, 10),
    Vector3( 100,  100, 10)
]

for i in range(0, len(points)):
    if i + 2 > len(points):
        drawLine(points[i].project(fov), points[0].project(fov))
    else :
        drawLine(points[i].project(fov), points[i + 1].project(fov))
