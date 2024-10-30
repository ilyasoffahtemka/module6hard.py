class Figure:
    sides_count = 0

    def __init__(self, color=(0, 0, 0), *sides):
        self.sides = sides if (len(sides) == self.sides_count
                               and self.__is_valid_sides(*sides)) else [1] * self.sides_count
        self.__color = list(color)
        self.filled = True

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r ,g, b):
        return all(isinstance(value, int) and 0 <= value <= 255 for value in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        return all(isinstance(side, int) and side > 0 for side in sides)

    def get_sides(self):
        return self.sides

    def __len__(self):
        return sum(self.sides)

    def set_sides(self):
        if len(new_sides) == self.sides_count and self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, color=(0, 0, 0), *sides):
        super().__init__(color,*sides)
        self.__radius = self.sides[0] / (2 * math.pi)

    def get_square(self):
        return  math.pi * self.__radius ** 2

import math

class Figure:
    sides_count = 0

    def __init__(self, color=(0, 0, 0), *sides):
        # Проверка на количество сторон и их корректность
        self.sides = sides if len(sides) == self.sides_count and self.__is_valid_sides(*sides) else [1] * self.sides_count
        self.__color = list(color)
        self.filled = True

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(value, int) and 0 <= value <= 255 for value in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        return all(isinstance(side, int) and side > 0 for side in sides)

    def get_sides(self):
        return self.sides

    def __len__(self):
        return sum(self.sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count and self.__is_valid_sides(*new_sides):
            self.sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color=(0, 0, 0), *sides):
        super().__init__(color, *sides)
        self.__radius = self.sides[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        # Формула Герона для площади треугольника
        s = sum(self.sides) / 2
        return math.sqrt(s * (s - self.sides[0]) * (s - self.sides[1]) * (s - self.sides[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color=(0, 0, 0), *sides):
        # Установка всех 12 сторон как одинаковых значений
        super().__init__(color, *([sides[0]] * 12 if len(sides) == 1 else sides))

    def get_volume(self):
        return self.sides[0] ** 3


circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)
circle1.set_color(55, 66, 77)
print(circle1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())
cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())
print(len(circle1))
print(cube1.get_volume())
