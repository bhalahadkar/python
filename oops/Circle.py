class Circle:
    pi = 3.14

    def __init__(self, radius = 1):
        self.radius = radius

    def getDiameter(self):
        return self.radius*2

    def getCircumference(self):
        return self.radius * self.pi * 2

    def getArea(self):
        return self.pi * self.radius**2


mycircle = Circle(2)
print(mycircle.getCircumference())