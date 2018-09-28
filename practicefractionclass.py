class Fraction:

    def __init__(self, top, bottom):
        self.numerator = top
        self.denominator = bottom

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)

myFraction = Fraction(3,5)
print(myFraction)




