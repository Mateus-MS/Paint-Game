from engine.draw import *

class Mesh:
    def __init__(self, vertex, edges):
        self.vertex = vertex
        self.edges = edges

    def rotate(self, direction, angle):
        
        if direction.x == 1:
            for i in range(len(self.vertex)):
                self.vertex[i] = self.vertex[i].RotateX(angle)
        if direction.y == 1:
            for i in range(len(self.vertex)):
                self.vertex[i] = self.vertex[i].RotateY(angle)
        if direction.z == 1:
            for i in range(len(self.vertex)):
                self.vertex[i] = self.vertex[i].RotateZ(angle)

    def render(self):

        projecteds = []

        for i in range(len(self.vertex)):
            projected = self.vertex[i].OrthographicProject()
            vector_projected = projected.forceToVector2()
            projecteds.append(vector_projected)

        for i in range(len(self.edges) - 1):
            drawLine(projecteds[self.edges[i]], projecteds[self.edges[i + 1]])
            i += 1