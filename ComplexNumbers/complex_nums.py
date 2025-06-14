import math
from typing import Tuple


class ComplexNum:

    def __init__(self, re=0, im=0) :
        self.re = re
        self.im = im

    def __str__(self): # выводить красиво
        return f"{self.re} + {self.im}·i"

    def __add__(self, num: 'ComplexNum') :
        result = ComplexNum(0,0)
        result.re = self.re + num.re
        result.im = self.im + num.im
        return result

    def __sub__(self, other: 'ComplexNum'):  # вычитание
        re = self.re - other.re
        im = self.im - other.im
        return ComplexNum(re, im)

    def __mul__(self, other: 'ComplexNum'):
        result = ComplexNum(0, 0)
        result.re = self.re * other.re - self.im * other.im
        result.im = self.re * other.im + self.im * other.re
        return result

    def __truediv__(self, other: 'ComplexNum') :
        denominator = other.re ** 2 + other.im ** 2  # знаменатель
        if denominator == 0:
            return None
        re = (self.re * other.re + self.im * other.im) / denominator
        im = (self.im * other.re - self.re * other.im) / denominator
        return ComplexNum(re, im)

    def __abs__(self) -> float:  # модуль
        return math.sqrt(self.re ** 2 + self.im ** 2)

    def conjugate(self):  # сопряженное
        return ComplexNum(self.re, - self.im)

    def to_polar(self) -> Tuple[float, float] : # в полярные координаты (ра
        r = abs(self)
        phi = math.atan2(self.im, self.re)
        return r, phi

    def inverse(self) :  # обратное
        denominator = self.re ** 2 + self.im ** 2  # знаменатель
        return ComplexNum(self.re / denominator, -self.im / denominator)

    def int_power(self, n: int) :  # степень целочисленная
        if n == 0:
            return ComplexNum(1, 0)
        if n < 0:
            return self.inverse().int_power(-n)
        result = ComplexNum(1, 0)
        x = self
        while n > 0:
            if n % 2 == 1:
                result = result * x
            x = x * x
            n = n // 2  # когда умножаем на само себя, уменьшаем нужную степень для возведения вдвое
        return result




def main() :
    z1 = ComplexNum(3, 5)
    z2 = ComplexNum(1, 2)
    z3 = z1  + z2

    print (z3)
    print(z1*z3)


if __name__ == '__main__' :
    main()