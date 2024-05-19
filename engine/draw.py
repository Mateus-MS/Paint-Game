import pyautogui as py
from maths.vector2 import Vector2

screenSize = Vector2(*py.size())

def drawPoint(vec):
    if not vec.isVector2:
        raise TypeError(f"Trying to use a {type(vec)} as cordinates at drawPoint.")
    py.click(*vec.convertZeroAtCenter(screenSize).arr)

def drawLine(vec1, vec2):
    if not vec1.isVector2:
        raise TypeError(f"Trying to use a {type(vec1)} as cordinates at drawLine.")
    if not vec2.isVector2:
        raise TypeError(f"Trying to use a {type(vec2)} as cordinates at drawLine.")
    
    py.mouseDown(*vec1.convertZeroAtCenter(screenSize).arr)
    py.mouseUp(*vec2.convertZeroAtCenter(screenSize).arr)