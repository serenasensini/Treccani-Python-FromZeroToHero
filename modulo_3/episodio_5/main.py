# Classe genitore con figlio

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    pass


# Override

class Polygon:
    def __init__(self, nbrsides):
        self.nbr_sides = nbrsides

    def whoamI(self):
        if self.nbr_sides == 3:
            return "Triangle"
        elif self.nbr_sides == 4:
            return "Rectangle"
        else:
            return "Polygon"

    def howmanysides(self):
        return self.nbr_sides

    def area(self):
        return "No Area"

    def perimeter(self):
        return "No Perimeter"


class Square(Polygon):

    def __init__(self):
        Polygon.__init__(self, 4)

    def area(self):
        area = self.side ** 2
        print('The area is equal to', str(area))

    def perimeter(self):
        perimeter = self.side * 4
        print('The perimeter is equal to', str(perimeter))


# Funzione super()

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)