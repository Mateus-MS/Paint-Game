from .vector2 import Vector2
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
    
    def project(self, fov):

        if not isinstance(fov, numbers.Number):
            raise TypeError(f"Trying to project with a {type(fov)} as FOV.")

        x = (self.x * fov) / (self.z + fov)
        y = (self.y * fov) / (self.z + fov)

        return Vector2(x, y)