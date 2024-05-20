from maths import Vector3
from engine.draw import *

class Cube:
    def __init__(self):

        self.vertex = [
            Vector3(-100,  100, 10),
            Vector3( 100,  100, 10),
            Vector3( 100, -100, 10),
            Vector3(-100, -100, 10),
            Vector3(-100,  100, 210),
            Vector3( 100,  100, 210),
            Vector3( 100, -100, 210),
            Vector3(-100, -100, 210)
        ]
        self.edges = [
            0, 1,
            1, 3,
            3, 0,

            1, 2,
            2, 3,
            3, 1,

            1, 5, 
            5, 2,
            2, 1,

            5, 6,
            6, 2,
            2, 5,

            4, 0,
            0, 7,
            7, 4,

            7, 0, 
            0, 3,
            3, 7,

            0, 1,
            1, 4,
            4, 0,

            1, 5,
            5, 4,
            4, 1,

            3, 2,
            2, 7,
            7, 3,

            2, 6,
            6, 7,
            7, 2
        ]

        self.angle = 0

    def render(self):

        projecteds = []

        for i in range(len(self.vertex)):
            rotated  = self.vertex[i].RotateY(self.angle)
            rotated  = rotated.RotateX(self.angle)
            rotated  = rotated.RotateZ(self.angle)
            projected = rotated.OrthographicProject()
            vector_projected  = projected.forceToVector2()
            projecteds.append(vector_projected)

        for i in range(len(self.edges) - 1):
            drawLine(projecteds[self.edges[i]], projecteds[self.edges[i + 1]])
            i += 1