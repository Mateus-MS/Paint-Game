from engine.draw import *
from .mesh import Mesh
from maths import Vector3

class Quad(Mesh):
    def __init__(self):
        self.vertex = [
            Vector3( 100,  100, 10),
            Vector3( 100, -100, 10),
            Vector3(-100, -100, 10),
            Vector3(-100,  100, 10)
        ]
        self.edges  = [
            0, 1,
            1, 2,
            2, 0,

            2, 3,
            3, 0, 
            0, 2
        ]