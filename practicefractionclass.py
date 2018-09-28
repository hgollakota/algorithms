class Fraction:

    def __init__(self, top, bottom):

        #Need to figure out how to check that both top and bottom are integers, and if they are to throw and exception

        def gcd(x, y):
            while y != 0:
                (x, y) = (y, x % y)
            return x
        common = gcd(top,bottom)
        self.numerator = top//common
        self.denominator = bottom//common

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)

    def __add__(self,otherFraction):
        newNumerator = self.numerator * otherFraction.denominator + self.denominator * otherFraction.numerator
        newDenominator = self.denominator * otherFraction.denominator
        return Fraction(newNumerator,newDenominator)

    def __sub__(self,otherFraction):
        newNumerator = self.numerator * otherFraction.denominator - otherFraction.numerator * self.denominator
        newDenominator = self.denominator * otherFraction.denominator
        return Fraction(newNumerator, newDenominator)

    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other):
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def __eq__(self, other):
        firstnum = self.numerator * other.denominator
        secondnum = other.numerator * self.denominator
        return firstnum == secondnum

    def __ne__(self, other):
        firstnum = self.numerator * other.denominator
        secondnum = other.numerator * self.denominator
        return not firstnum == secondnum

    def __gt__(self, other):
        firstnum = self.numerator / self.denominator
        secondnum = other.numerator / other.denominator
        return firstnum > secondnum

    def __lt__(self, other):
        firstnum = self.numerator / self.denominator
        secondnum = other.numerator / other.denominator
        return firstnum < secondnum

    def __ge__(self, other):
        firstnum = self.numerator / self.denominator
        secondnum = other.numerator / other.denominator
        return firstnum >= secondnum

    def __le__(self, other):
        firstnum = self.numerator / self.denominator
        secondnum = other.numerator / other.denominator
        return firstnum <= secondnum

    def getNum(self):
        return self.numerator

    def getDen(self):
        return self.denominator



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

#try getNum and getDen functions
print(f6.getNum())
print(f6.getDen())

#reducing fraction
print(Fraction(75,100))

#subtraction, multiplication and division override
print("1/4 - 3/4 =", Fraction(1,4) - Fraction(3,4))
print("1/3 * 1/2 =", Fraction(1,3) * Fraction(1,2))
print("1/7 / 1/7 =", Fraction(1,7) / Fraction(1,7))






