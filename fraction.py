class Fraction(object):
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def simplify(self):
        flag = False
        if self.num < 0:
            self.num *= -1
            flag = True
        for i in range(self.num, 0, -1):
            if self.num % i == 0 and self.den % i == 0:
                self.num = int(self.num / i)
                self.den = int(self.den / i)
        if flag:
            self.num *= -1
        return Fraction(self.num, self.den)

    def __add__(self, other):
        sum_den = self.den * other.den
        sum_num = (other.den * self.num) + (self.den * other.num)
        return Fraction(sum_num, sum_den).simplify()

    def __sub__(self, other):
        sub_den = self.den * other.den
        sub_num = (other.den * self.num) - (self.den * other.num)
        return Fraction(sub_num, sub_den).simplify()

    def __mul__(self, other):
        mul_den = self.den * other.den
        mul_num = self.num * other.num
        return Fraction(mul_num, mul_den).simplify()

    def __truediv__(self, other):
        div_num = self.num * other.den
        div_den = self.den * other.num
        return Fraction(div_num, div_den).simplify()

    def __eq__(self, other):
        self = self.simplify()
        other = other.simplify()
        if self.num == other.num and self.den == other.den:
            return True
        else:
            return False

    def __lt__(self, other):
        if (self.num / self.den) < (other.num / other.den):
            return True
        else:
            return False


f = Fraction(3, 4)
f2 = Fraction(1, 2)
f3 = Fraction(4, 13)
f4 = Fraction(3, 7)
f5 = Fraction(5, 6)
f6 = Fraction(12, 16)

print(f + f2)  # 5/4
print(f3 + f4)  # 67/91
print(f5 + f)  # 19/12

print(f - f2)  # 1/4
print(f3 - f4)  # -11/91
print(f5 - f)  # 1/12

print(f * f2)  # 3/8
print(f3 * f4)  # 12/91
print(f5 * f)  # 5/8

print(f / f2)  # 3/2
print(f3 / f4)  # 28/39
print(f5 / f)  # 10/9

print(f == f2)  # False
print(f == f6)  # True

print(f < f2)  # False
print(f3 < f4)  # True
print(f5 < f)  # False

print(f > f2)  # True
print(f3 > f4)  # False
print(f5 > f)  # True

print(f6.simplify())  # 3/4
print(Fraction.simplify(f6))  # 3/4 Same method, different syntax
