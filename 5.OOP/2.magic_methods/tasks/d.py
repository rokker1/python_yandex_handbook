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
            self.__normalize()
        else:
            args = arga.split("/")
            self.n = int(args[0])
            self.d = int(args[1])
            self.__normalize()

    def __str__(self):
        return f"{self.n}/{self.d}"

    def __repr__(self):
        return f"Fraction({self.n}, {self.d})"

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
        gcd_ = self.__gcd(self.n, self.d)
        self.n //= gcd_
        self.d //= gcd_

        
fraction_a = Fraction("54/6")
fraction_b = Fraction(5, 135)
print(fraction_a)
fraction = Fraction(3, 9)
print(fraction, repr(fraction))
fraction = Fraction('7/14')
print(fraction, repr(fraction))


fraction = Fraction(3, 210)
print(fraction, repr(fraction))
fraction.numerator(2)
fraction.numerator(10)
print(fraction.numerator(), fraction.denominator())
fraction.denominator(2)
print(fraction.numerator(), fraction.denominator())
