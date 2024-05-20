from maths import Vector3
from engine.draw import *
from .mesh import Mesh

class Cube(Mesh): 
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