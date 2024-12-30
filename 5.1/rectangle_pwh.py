ACCURACY = 2


def round_answer(func, round_accuracy: int | None = ACCURACY):
    def new_func(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        if isinstance(result, tuple):
            return tuple(round(val, round_accuracy) for val in result)
        elif isinstance(result, (float, int)):
            return round(result, round_accuracy)
        return result  
    return new_func


class Rectangle():
    """
    Rectangle:
        - Left upper vertex
        - Width
        - Height
    """
    def __init__(self,
                 point_1: tuple,
                 point_2: tuple = None,
                 width: int | float = None,
                 height: int | float = None):
        """Create rectange with
            - One vertex (left & upper), width and height
            - Two opposite vertices

        Args:
            point_1 (tuple): 1 of 4 verticies. Defaults to None.
            point_2 (tuple, optional): Opposite vertex. Defaults to None.
            width (int | float, optional): Width. Defaults to None.
            height (int | float, optional): Height. Defaults to None.
        """
        # Vertex, width, height case
        if (isinstance(point_1, tuple) and 
                isinstance(width, (int, float)) and 
                isinstance(height, (int, float))):
            self.point = (point_1[0], point_1[0])
            self.width = width 
            self.height = height           

        # Vertex and Opposite Vertex case
        elif (isinstance(point_1, tuple) and 
              isinstance(point_1, tuple)):
            self.point = min(point_1[0], point_2[0]), max(point_1[1], point_2[1])
            self.width = abs(point_2[0] - point_1[0])
            self.height = abs(point_1[1] - point_2[1])

        else:
            raise ValueError("Can't Init Rectange: Wrong Arguments")
        
    @round_answer
    def area(self) -> float:
        return self.width * self.height
    
    @round_answer
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)
    
    @round_answer
    def get_pos(self) -> tuple:
        """Rectangle position as left-upper point
        """
        return self.point

    @round_answer
    def get_size(self) -> tuple:
        return (self.width, self.height)
    
    def move(self, dx, dy) -> None:
        self.point = round(self.point[0] + dx, ACCURACY), round(self.point[1] + dy, ACCURACY)

    def resize(self, width, height) -> None:
        self.width = round(width, ACCURACY)
        self.height = round(height, ACCURACY)

    @round_answer
    def get_center(self) -> tuple:
        """Return center of rectangle as double coords

        Returns:
            tuple: coords (x, y)
        """
        return (self.point[0] + round(self.width / 2, ACCURACY), 
                self.point[1] + round(self.height / 2, ACCURACY))

    def turn(self) -> None:
        """Change rectangle dirrection around center
        """
        dm = round(round(self.width - self.height, 2) / ACCURACY, ACCURACY)
        self.move(dm, dm)
        self.width, self.height = self.height, self.width

    def scale(self, factor: int | float | None = 1) -> None:
        """Change rectangle scale around center
        """
        center = self.get_center()
        dx = round(self.point[0] - center[0], ACCURACY) * (factor - 1)
        dy = round(self.point[1] - center[1], ACCURACY) * (factor - 1)
        self.point = (round(self.point[0] + round(dx, ACCURACY), ACCURACY), 
                      round(self.point[1] - round(dy, ACCURACY), ACCURACY))
        self.width, self.height = (round(self.width * factor, ACCURACY), 
                                   round(self.height * factor, ACCURACY))


def main():
    rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
    print(rect.get_pos(), rect.get_size(), sep='\n')
    rect.turn()
    print(rect.get_pos(), rect.get_size(), sep='\n')


if __name__ == "__main__":
    main()