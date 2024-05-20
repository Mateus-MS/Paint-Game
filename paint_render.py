import pyautogui as py
import keyboard
from time import sleep

from engine.draw import *
from maths import Vector2
from maths import Vector3

from engine.objects.mesh import Mesh
from engine.objects.cube import Cube
from engine.objects.triangle import Triangle
from engine.objects.quad import Quad

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
    cube.rotate(Vector3(1, 1, 1), 0.1)

    sleep(.15)