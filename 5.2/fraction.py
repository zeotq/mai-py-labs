from math import gcd, lcm


class Fraction(object):
    def __init__(self, *args):
        # Init with two int: num & den
        if len(args) == 2 and type(args[0]) is int and type(args[1]) is int:
            self.__num = args[0]
            self.__den = args[1]
        # Init with str with separator "/"
        elif len(args) == 1 and type(args[0]) is str and "/" in args[0]:
            self.__num, self.__den = tuple(map(int, args[0].split("/")))
        # Init with one int in str format: num
        elif len(args) == 1 and type(args[0]) is str and args[0].isdigit():
            self.__num, self.__den = int(args[0]), 1
        # Init with one int in int format: num
        elif len(args) == 1 and type(args[0]) is int:
            self.__num, self.__den = args[0], 1
        else:
            raise ValueError
        
        if self.__den == 0: 
            raise ZeroDivisionError

        # Task 5 / The conventionality of the task
        self.__sign = 1

        # Simplyfy Fraction
        self.__shorten()

    def __shorten(self):
        if self.__num == 0:
            self.__den = 1
            self.__sign = 1
            return
        self.__sign = -1 if self.__sign * self.__num * self.__den < 0 else 1
        self.__num, self.__den = abs(self.__num), abs(self.__den)

        gcd_value = gcd(self.__num, self.__den)
        self.__num //= gcd_value
        self.__den //= gcd_value

        # if self.__den < 0:
        #     self.__num *= -1
        #     self.__den *= -1

    def numerator(self, number: int = None):
        """Изменяет значение числителя и производит сокращение дроби, если это необходимо"""
        if number is None:
            return self.__num
        if not isinstance(number, int):
            raise ValueError
        self.__num = number
        self.__shorten()

    def denominator(self, number: int = None):
        """Изменяет значение знаменателя и производит сокращение дроби, если необходимо"""
        if number is None:
            return self.__den
        if not isinstance(number, int):
            raise ValueError
        if number == 0:
            raise ZeroDivisionError
        self.__den = number
        self.__shorten()

    def reverse(self):
        return Fraction(self.__den * self.__sign, self.__num)

    def __str__(self):
        """Возвращает строковое представление дроби в формате <числитель>/<знаменатель>"""
        return f'{self.__sign * self.__num}/{self.__den}'

    def __repr__(self):
        """Возвращает описание объекта в формате Fraction(<числитель>/<знаменатель>)."""
        return f"Fraction('{self.__sign * self.__num}/{self.__den}')"  # Task 5
    
        """Возвращает описание объекта в формате Fraction(<числитель>, <знаменатель>)."""
        return f'Fraction({self.__num}, {self.__den})'  # Task 4

    def __neg__(self):
        return Fraction(-1 * self.__sign * self.__num, self.__den)

    def __add__(self, other):
        if isinstance(other, Fraction):
            lcm_value = lcm(self.__den, other.__den)
            new_self_num = self.__sign * self.__num * (lcm_value // self.__den)
            new_other_num = other.__sign * other.__num * (lcm_value // other.__den)
            return Fraction(new_self_num + new_other_num, lcm_value)
        if isinstance(other, (int, float)):
            other = int(other)
            return Fraction(self.__sign * self.__num + other * self.__den, self.__den)
        if isinstance(other, str):
            return self.__add__(Fraction(other))
        raise ValueError

    def __radd__(self, other):
        if isinstance(other, (int, float)):
            other = int(other)
            return Fraction(self.__sign * self.__num + other * self.__den, self.__den)
        if isinstance(other, str):
            return self.__add__(Fraction(other))
        raise ValueError

    def __iadd__(self, other):
        if isinstance(other, Fraction):
            lcm_value = lcm(self.__den, other.__den)
            new_snum = self.__sign * self.__num * (lcm_value // self.__den)
            new_onum = other.__sign * other.__num * (lcm_value // other.__den)
            self.__num = new_snum + new_onum
            self.__den = lcm_value
            self.__sign = 1
            self.__shorten()
            return self
        if isinstance(other, (int, float)):
            other = int(other)
            self.__num = self.__num * self.__sign + other * self.__den
            self.__sign = 1
            self.__shorten()
            return self
        if isinstance(other, str):
            return self.__iadd__(Fraction(other))
        
        raise ValueError

    def __sub__(self, other):
        if isinstance(other, Fraction):
            lcm_value = lcm(self.__den, other.__den)
            new_snum = self.__sign * self.__num * (lcm_value // self.__den)
            new_onum = other.__sign * other.__num * (lcm_value // other.__den)
            return Fraction(new_snum - new_onum, lcm_value)
        if isinstance(other, (int, float)):
            other = int(other)
            return Fraction(self.__sign * self.__num - other * self.__den, self.__den)
        if isinstance(other, str):
            return self.__sub__(Fraction(other))
        
        raise ValueError

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            other = int(other)
            return Fraction(other * self.__den - self.__sign * self.__num, self.__den)
        if isinstance(other, str):
            return self.__rsub__(Fraction(other))
        
        raise ValueError

    def __isub__(self, other):
        if isinstance(other, Fraction):
            lcm_value = lcm(self.__den, other.__den)
            new_snum = self.__sign * self.__num * (lcm_value // self.__den)
            new_onum = other.__sign * other.__num * (lcm_value // other.__den)
            self.__num = new_snum - new_onum
            self.__den = lcm_value
            self.__sign = 1
            self.__shorten()
            return self
        if isinstance(other, (int, float)):
            other = int(other)
            self.__num = self.__num * self.__sign - other * self.__den
            self.__sign = 1
            self.__shorten()
            return self
        if isinstance(other, str):
            return self.__isub__(Fraction(other))
        
        raise ValueError

    def __mul__(self, other):
        if isinstance(other, Fraction):
            new_num = self.__num * other.__num * self.__sign * other.__sign
            new_den = self.__den * other.__den
            return Fraction(new_num, new_den)
        if isinstance(other, (int, float)):
            other = int(other)
            return Fraction(self.__num * self.__sign * other, self.__den)
        if isinstance(other, str):
            return self.__mul__(Fraction(other))
        
        raise ValueError

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            other = int(other)
            return Fraction(self.__num * self.__sign * other, self.__den)
        if isinstance(other, str):
            return self.__mul__(Fraction(other))
        
        raise ValueError

    def __imul__(self, other):
        if isinstance(other, Fraction):
            self.__num = self.__num * other.__num * self.__sign * other.__sign
            self.__den = self.__den * other.__den
            self.__sign = 1
            self.__shorten()
            return self
        if isinstance(other, (int, float)):
            other = int(other)
            self.__num = self.__num * self.__sign * other
            self.__sign = 1
            self.__shorten()
            return self
        if isinstance(other, str):
            return self.__imul__(Fraction(other))
        
        raise ValueError

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            new_num = self.__num * other.__den * self.__sign * other.__sign
            new_den = self.__den * other.__num
            return Fraction(new_num, new_den)
        if isinstance(other, (int, float)):
            other = int(other)
            return Fraction(self.__num * self.__sign, self.__den * other)
        if isinstance(other, str):
            return self.__truediv__(Fraction(other))
        
        raise ValueError

    def __rtruediv__(self, other):
        if isinstance(other, (int, float)):
            other = int(other)
            new_den = self.__num * self.__sign
            if new_den == 0:
                raise ZeroDivisionError
            return Fraction(self.__den * other, new_den)
        if isinstance(other, str):
            return self.__rtruediv__(Fraction(other))
        
        raise ValueError

    def __itruediv__(self, other):
        if isinstance(other, Fraction):
            self.__num = self.__num * other.__den * self.__sign * other.__sign
            self.__den = self.__den * other.__num
            self.__sign = 1
            self.__shorten()
            return self
        if isinstance(other, (int, float)):
            other = int(other)
            self.__num = self.__num * self.__sign
            self.__den = self.__den * other
            self.__sign = 1
            self.__shorten()
            return self
        if isinstance(other, str):
            return self.__itruediv__(Fraction(other))
        
        raise ValueError

    def __lt__(self, other) -> bool:  # <
        if isinstance(other, Fraction):
            return self.__num * self.__sign * other.__den < other.__num * other.__sign * self.__den
        if isinstance(other, (int, float)):
            other = int(other)
            return self.__num * self.__sign < self.__den * other
        if isinstance(other, str):
            return self.__lt__(Fraction(other))
        raise ValueError

    def __le__(self, other) -> bool:  # <=
        if isinstance(other, Fraction):
            return self.__num * self.__sign * other.__den <= other.__num * other.__sign * self.__den
        if isinstance(other, (int, float)):
            other = int(other)
            return self.__num * self.__sign <= self.__den * other
        if isinstance(other, str):
            return self.__le__(Fraction(other))
        raise ValueError

    def __eq__(self, other) -> bool:  # ==
        if isinstance(other, Fraction):
            return self.__num * self.__sign * other.__den == other.__num * other.__sign * self.__den
        if isinstance(other, (int, float)):
            other = int(other)
            return self.__num * self.__sign == self.__den * other
        if isinstance(other, str):
            return self.__eq__(Fraction(other))
        raise ValueError

    def __ne__(self, other) -> bool:  # !=
        if isinstance(other, Fraction):
            return self.__num * self.__sign * other.__den != other.__num * other.__sign * self.__den
        if isinstance(other, (int, float)):
            other = int(other)
            return self.__num * self.__sign != self.__den * other
        if isinstance(other, str):
            return self.__ne__(Fraction(other))
        raise ValueError

    def __gt__(self, other) -> bool:  # >
        if isinstance(other, Fraction):
            return self.__num * self.__sign * other.__den > other.__num * other.__sign * self.__den
        if isinstance(other, (int, float)):
            other = int(other)
            return self.__num * self.__sign > self.__den * other
        if isinstance(other, str):
            return self.__gt__(Fraction(other))
        raise ValueError

    def __ge__(self, other) -> bool:  # >=
        if isinstance(other, Fraction):
            return self.__num * self.__sign * other.__den >= other.__num * other.__sign * self.__den
        if isinstance(other, (int, float)):
            other = int(other)
            return self.__num * self.__sign >= self.__den * other
        if isinstance(other, str):
            return self.__ge__(Fraction(other))
        raise ValueError


def main():
    a = Fraction('0')
    b = Fraction('-14/15')
    print(b > 0 > Fraction("100"))
    print(a)


if __name__ == "__main__":
    main()
