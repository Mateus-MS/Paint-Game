import numbers

class Vector2:
    def __init__(self, x, y):

        if not isinstance(x, numbers.Number):
            raise TypeError(f"Trying to create a vector3 with a: {type(x)} at X.")
        if not isinstance(y, numbers.Number):
            raise TypeError(f"Trying to create a vector3 with a: {type(y)} at Y.")

        self._x = x
        self._y = y
        self.arr = (x, y)
        self.isVector2 = True

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

    def print(self):
        print(f'x: {self.x}, y: {self.y}')

    def add(self, value):
        if isinstance(value, numbers.Number):
            return Vector2(self.x + value, self.y + value)
        if not value.isVector2:
            raise TypeError(f"Trying to add a {type(value)} to a Vector2.")
        return Vector2(self.x + value.x, self.y + value.y)
    
    def div(self, value):
        if isinstance(value, numbers.Number):
            return Vector2(self.x / value, self.y / value)
        if not value.isVector:
            raise TypeError(f"Tying to divide a {type(value)} by a Vector2.")
        
        return Vector2(self.x / value.x, self.y / value.y)
    
    def convertZeroAtCenter(self, screen):
        if not screen.isVector2:
            raise TypeError(f"Trying to convert at center with a {type(screen)} as screen.")
        return Vector2(*self.add(screen.div(2)).arr)