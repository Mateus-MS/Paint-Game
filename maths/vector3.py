from .vector2 import Vector2
from .matrix import Matrix
import math
import numbers

class Vector3:
    def __init__(self, x, y, z):

        if not isinstance(x, numbers.Number):
            raise TypeError(f"Trying to create a vector3 with a: {type(x)} at X.")
        if not isinstance(y, numbers.Number):
            raise TypeError(f"Trying to create a vector3 with a: {type(y)} at Y.")
        if not isinstance(z, numbers.Number):
            raise TypeError(f"Trying to create a vector3 with a: {type(z)} at Z.")
        
        self._x = x
        self._y = y
        self._z = z
        self.isVector3 = True
        self.arr = [x, y, z]

    def __get_x(self):
        return self._x

    def __set_x(self, value):
        if not isinstance(value, numbers.Number):
            raise TypeError("The value must be a int")
        self._x = value
        self.arr[0] = value

    x = property(__get_x, __set_x)

    def __get_y(self):
        return self._y
    
    def __set_y(self, value):
        if not isinstance(value, numbers.Number):
            raise TypeError("The value must be a int")
        self._y = value
        self.arr[1] = value
    
    y = property(__get_y, __set_y)

    def __get_z(self):
        return self._z
    
    def __set_z(self, value):
        if not isinstance(value, numbers.Number):
            raise TypeError("The value must be a int")
        self._z = value
        self.arr[2] = value
    
    z = property(__get_z, __set_z)


    def print(self):
        print(f'x: {self.x}, y: {self.y}, z: {self.z}')

    def forceToVector2(self):
        return Vector2(self.x, self.y)
    
    def OrthographicProject(self):
        projectionMatrix = Matrix([ 
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ])

        vecMat    = self.convertToMatrix()
        projected = projectionMatrix.mul(vecMat)
        vec_projected = Vector3(projected.matrix[0][0], projected.matrix[1][0], projected.matrix[2][0])

        return vec_projected
    
    def RotateZ(self, angle):
        if not isinstance(angle, numbers.Number):
            raise TypeError(f"Trying to project with a {type(angle)} as Angle.")

        rotationMatrix = Matrix([ 
            [math.cos(angle), -math.sin(angle), 0],
            [math.sin(angle),  math.cos(angle), 0],
            [0, 0, 1]
        ])

        rotated = rotationMatrix.mul(self.convertToMatrix())
        vec_rotated = Vector3(rotated.matrix[0][0], rotated.matrix[1][0], rotated.matrix[2][0])
        return vec_rotated
    
    def RotateX(self, angle):
        if not isinstance(angle, numbers.Number):
            raise TypeError(f"Trying to project with a {type(angle)} as Angle.")

        rotationMatrix = Matrix([ 
            [1, 0, 0],
            [0, math.cos(angle), -math.sin(angle)],
            [0, math.sin(angle),  math.cos(angle)]
        ])

        rotated = rotationMatrix.mul(self.convertToMatrix())
        vec_rotated = Vector3(rotated.matrix[0][0], rotated.matrix[1][0], rotated.matrix[2][0])
        return vec_rotated
    
    def RotateY(self, angle):
        if not isinstance(angle, numbers.Number):
            raise TypeError(f"Trying to project with a {type(angle)} as Angle.")

        rotationMatrix = Matrix([ 
            [math.cos(angle), 0, -math.sin(angle)],
            [0, 1, 0],
            [math.sin(angle), 0,  math.cos(angle)]
        ])

        rotated = rotationMatrix.mul(self.convertToMatrix())
        vec_rotated = Vector3(rotated.matrix[0][0], rotated.matrix[1][0], rotated.matrix[2][0])
        return vec_rotated

    # def Rotate(self, direction, angle):


    def convertToMatrix(self):
        return Matrix([
            [self.x],
            [self.y],
            [self.z]
        ])