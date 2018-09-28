class Fraction:

    def __init__(self, top, bottom):
        self.numerator = top
        self.denominator = bottom

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)

    def __add__(self,otherFraction):
        newNumerator = self.numerator * otherFraction.denominator + self.denominator * otherFraction.numerator
        newDenominator = self.denominator * otherFraction.denominator
        def gcd(x, y):
            while y != 0:
                (x, y) = (y, x % y)
            return x
        common = gcd(newNumerator,newDenominator)
        return Fraction(newNumerator//common,newDenominator//common)

    def __eq__(self, other):
        firstnum = self.numerator * other.denominator
        secondnum = other.numerator * self.denominator
        return firstnum == secondnum


#playing around with the string override in the class
myFraction = Fraction(3,5)
print(myFraction)
print("I ate", myFraction, "of my pizza")

#testing out adding and reducing fractions
fraction1 = Fraction(3,5)
fraction2 = Fraction(1,10)
fraction3 = fraction1 + fraction2
print(fraction3)

#Checking deep equality of fractions
f4 = Fraction(2,5)
f5 = Fraction(1,10)
f6 = f4 + Fraction(3,10)
if f4 == f6:
    print("they're equal")
else:
    print("they're not equal!")

print((f5+f5+f5+f5)==f4)
