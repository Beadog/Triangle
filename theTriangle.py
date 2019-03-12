'''
Corrie Stewart
Program calculates triangle area and perimeter
Date: 10/14/18
'''

class GeometricObject:
    def __init__(self, color =  "green" , filled = True):
        self.__color = color
        self.__filled = filled

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def isFilled(self):
        return self.__filled

    def setFilled(self, filled):
        self.__filled = filled

    def __str__(self):
        return  "color: "  + self.__color + \
             " and filled: "  + str(self.__filled)


class Triangle(GeometricObject):
    def __init__(self, side1 = 1.0 , side2 = 1.0, side3 = 1.0):
        super().__init__()
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

    def getSide1(self):
        return self.__side1

    def setSide1(self, side1):
        self.__side1 = side1

    def getSide2(self):
        return self.__side2

    def setSide2(self, side2):
        self.__side2 = side2

    def getSide3(self):
        return self.__side3

    def setSide3(self, side3):
        self.__side3 = side3

    def setArea(self):
        self.area = area

    def getArea(self):
        s = (self.__side1 + self.__side2 + self.__side3) / 2
        area = (s * (s - self.__side1) * (s - self.__side2) * (s - self.__side3)) ** 0.5
        return area

    def getPerimeter(self):
        perimeter = self.__side1 + self.__side2 + self.__side3
        return  perimeter

    def triangleString(self):
        return "Triangle: Side 1: " + self.__side1 + "Side 2: " + self.__side2 + "Side 3: " + self.__side3

def main():
    side1 = eval(input("Enter a number for side 1: "))
    side2 = eval(input("Enter a number for side 2: "))
    side3 = eval(input("Enter a number for side 3: "))
    color = input("Enter a color for the triangle: ")
    filled = input("To fill the triangle, enter 1, otherwise enter 0: ")
    filledTrue = (filled == "1")
    #set the variables in the classes
    triangleSolution = Triangle(side1, side2, side3)  # this sets the triangle sides in Triangle Class
    triangleSolution.setColor(color)  # this sets the color in the superclass (through subclass)
    triangleSolution.setFilled(filledTrue) # this sets the fill
    #get the variables in the classes with printout
    print("The triangle’s area is: ", triangleSolution.getArea())
    print("The perimeter is: ", triangleSolution.getPerimeter())
    print("The color is: ", triangleSolution.getColor())
    print("The color is filled: ", triangleSolution.isFilled())

main()
