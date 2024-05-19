from engine.draw import *

class Triangle:

    def __init__(self, p1, p2, p3):
        if not p1.isVector3:
            raise TypeError(f"Trying to create a Triangle with the P1 using a {type(p1)}.")
        if not p2.isVector3:
            raise TypeError(f"Trying to create a Triangle with the P2 using a {type(p2)}.")
        if not p3.isVector3:
            raise TypeError(f"Trying to create a Triangle with the P3 using a {type(p3)}.")
        
        self.vertex = [
            p1, p2, p3
        ]

    def render(self, fov):
        drawLine(self.vertex[0].project(fov), self.vertex[1].project(fov))
        drawLine(self.vertex[1].project(fov), self.vertex[2].project(fov))
        drawLine(self.vertex[2].project(fov), self.vertex[0].project(fov))