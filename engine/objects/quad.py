from engine.draw import *

class Quad:
    def __init__(self, *vertex):
        self.vertex = [*vertex]
        self.edges  = [
            0, 1,
            1, 2,
            2, 0,

            2, 3,
            3, 0, 
            0, 2
        ]
        self.angle = 0

    def render(self):

        projecteds = []

        for i in range(len(self.vertex)):
            projected = self.vertex[i].OrthographicProject()
            rotated  = projected.RotateX(self.angle)
            rotated  = rotated.RotateY(self.angle)
            rotated  = rotated.RotateZ(self.angle)
            vector_projected  = rotated.forceToVector2()
            projecteds.append(vector_projected)

        for i in range(len(self.edges) - 1):
            drawLine(projecteds[self.edges[i]], projecteds[self.edges[i + 1]])
            i += 1