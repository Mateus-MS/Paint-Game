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
        self.angle = 0

    def render(self):

        p1_projected = self.vertex[0].OrthographicProject()
        p1_rotated   = p1_projected.RotateY(self.angle)
        p1_as_vec2   = p1_rotated.forceToVector2()

        p2_projected = self.vertex[1].OrthographicProject()
        p2_rotated   = p2_projected.RotateY(self.angle)
        p2_as_vec2   = p2_rotated.forceToVector2()

        p3_projected = self.vertex[2].OrthographicProject()
        p3_rotated   = p3_projected.RotateY(self.angle)
        p3_as_vec2   = p3_rotated.forceToVector2()

        drawLine(p1_as_vec2, p2_as_vec2)
        drawLine(p2_as_vec2, p3_as_vec2)
        drawLine(p3_as_vec2, p1_as_vec2)