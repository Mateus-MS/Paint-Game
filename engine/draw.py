import pyautogui as py
from maths.vector2 import Vector2

screenSize = Vector2(*py.size())

def drawPoint(value):
    if not value.isVector2:
        raise TypeError(f"Trying to use a {type(value)} as cordinates at drawPoint.")
    py.click(*value.convertZeroAtCenter(screenSize).arr)

def drawLine(v1, v2):
    if not v1.isVector2:
        raise TypeError(f"Trying to use a {type(v1)} as cordinates at drawLine.")
    if not v2.isVector2:
        raise TypeError(f"Trying to use a {type(v2)} as cordinates at drawLine.")
    
    py.mouseDown(*v1.convertZeroAtCenter(screenSize).arr)
    py.mouseUp(*v2.convertZeroAtCenter(screenSize).arr)