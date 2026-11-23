class Fraction:
    def __init__(self, num1, num2):
        self.nominator = num1
        self.denominator = num2
    def simply(self):
        temp1 = self.nominator
        temp2 = self.denominator
        while temp1 != temp2:
            if temp1 > temp2:
                temp1 = temp1 - temp2
            else:
                temp2 = temp2 - temp1
        if temp1 != 1:
            self.nominator = self.nominator // temp1
            self.denominator = self.denominator // temp1
    def __str__ (self):
        return f"{self.nominator}/{self.denominator}" 

    def __add__(self, other):
        temp = Fraction(self.nominator * other.denominator + other.nominator * self.denominator, self.denominator * other.denominator)
        temp.simply()
        return temp

    def __mul__ (self, other):
        temp = Fraction(self.nominator * other.nominator, self.denominator * other.denominator)
        temp.simply()
        return temp

    def __truediv__ (self, other):
        temp = Fraction(self.nominator * other.denominator, self.denominator * other.nominator)
        temp.simply()
        return temp

    def __eq__ (self, other):
        if self.nominator * other.denominator != other.nominator * self.denominator:
            return True

a = Fraction(1,2)
b = Fraction(3,7)
d = Fraction(7,6)
a.simply()
b.simply()
print(a)
print(b)
c = a/b
print(c == d)
