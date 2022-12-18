class Fraction:

    def __gcd(self, a, b):
        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a
        return a + b
    
    def __init__(self, arga=0, argb=None):
        if argb is not None:
            self.n = arga
            self.d = argb
        else:
            args = arga.split("/")
            self.n = int(args[0])
            self.d = int(args[1])
        self.__normalize()

    def __str__(self):
        return f"{self.n}/{self.d}"

    def __repr__(self):
        return f"Fraction('{self.n}/{self.d}')"

    def numerator(self, number=None):
        if number is None:
            return self.n
        self.n = number
        self.__normalize()

    def denominator(self, number=None):
        if number is None:
            return self.d
        self.d = number
        self.__normalize()

    def __normalize(self):
        if self.n >= 0 and self.d < 0 or\
            self.n < 0 and self.d > 0:
            segn = -1
        else:
            segn = 1
        self.n, self.d = abs(self.n), abs(self.d)
        gcd_ = self.__gcd(self.n, self.d)
        self.n = self.n // gcd_ * segn
        self.d //= gcd_


    def __neg__(self):
        copy_fraction = eval(self.__repr__())
        copy_fraction.n *= -1
        return copy_fraction
        
a = Fraction(1, 3)
b = Fraction(-2, -6)
c = Fraction(-3, 9)
d = Fraction(4, -12)
print(a, b, c, d)
print(*map(repr, (a, b, c, d)))
