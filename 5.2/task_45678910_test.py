from fraction import *

# Task 1
def test_init_1():
    fraction = Fraction(3, 9)
    assert str(fraction) == "1/3"
    assert repr(fraction) in ["Fraction(1, 3)", "Fraction('1/3')"]
    fraction = Fraction('7/14')
    assert str(fraction) == "1/2"
    assert repr(fraction) in ["Fraction(1, 2)", "Fraction('1/2')"]

def test_shorten_1():
    fraction = Fraction(3, 210)
    assert str(fraction) == "1/70"
    assert repr(fraction) in ["Fraction(1, 70)", "Fraction('1/70')"]
    fraction.numerator(10)
    assert fraction.numerator() == 1
    assert fraction.denominator() == 7
    fraction.denominator(2)
    assert fraction.numerator() == 1
    assert fraction.denominator() == 2

# Task 2
def test_negative_values():
    a = Fraction(1, 3)
    b = Fraction(-2, -6)
    c = Fraction(-3, 9)
    d = Fraction(4, -12)
    assert (str(a), str(b), str(c), str(d)) == ("1/3", "1/3", "-1/3", "-1/3")

def test_unar_minus():
    a = Fraction('-1/2')
    b = -a
    assert str(a) == '-1/2'
    assert str(b) == '1/2'
    assert (a is b) == False

    b.numerator(-b.numerator())
    a.denominator(-3)
    assert str(a) == '1/3' and str(b) == '-1/2'
    assert a.numerator() == 1 and a.denominator() == 3
    assert b.numerator() == 1 and  b.denominator() == 2

# Task 3
def test_add_one_class():
    a = Fraction(1, 3)
    b = Fraction(1, 2)

    c = a + b
    assert str(a) == "1/3"
    assert str(b) == "1/2"
    assert str(c) == "5/6"

    c += a
    assert str(c) == "7/6"
    assert (a is c) == False
    assert (b is c) == False

def test_sub_one_class():
    a = Fraction(1, 8)
    c = b = Fraction(3, 8)

    b -= a
    assert str(a) == "1/8"
    assert str(b) == "1/4"
    assert str(c) == "1/4"
    assert (b is c) == True
    c = c - b
    assert str(c) == "0/1"

def test_add_int():
    a = Fraction(1, 3)
    a = a + 1
    assert str(a) == "4/3"
    a += 1
    assert str(a) == "7/3"

def test_sub_int():
    a = Fraction(1, 3)
    a = a - 1
    assert str(a) == "-2/3"
    a -= 1
    assert str(a) == "-5/3"

# Task 4
def test_reverse():
    assert str(Fraction(2, 3).reverse()) == str(Fraction(3, 2))

def test_mul():
    a = Fraction(1, 3)
    b = Fraction(1, 2)
    c = a * b
    assert str(c) == "1/6" 
    assert (a is c) == False
    assert (b is c) == False
    c *= 2
    assert str(c) == "1/3" 
    c *= -2
    assert str(c) == "-2/3"

def test_div():
    a = Fraction(1, 3)
    b = Fraction(2, 1).reverse()
    b /= a
    assert str(a) == "1/3"
    assert str(b) == "3/2"
    c = Fraction("-1/2")
    d = b / c
    assert str(d) == "-3/1"

# Task 5
def test_comparison_1():
    a = Fraction(1, 3)
    b = Fraction(1, 2)
    assert (a > b) == False
    assert (a < b) == True
    assert (a >= b) == False
    assert (a <= b) == True
    assert (a == b) == False

def test_comparison_2():
    a = Fraction(1, 3)
    b = Fraction(-1, 2)
    assert (a > b) == True
    assert (a < b) == False
    assert (a >= b) == True
    assert (a <= b) == False
    assert (a == b) == False

def test_comparison_3():
    a = Fraction(1, 3)
    b = Fraction(3, 9)
    assert (a > b) == False
    assert (a < b) == False
    assert (a >= b) == True
    assert (a <= b) == True
    assert (a == b) == True
    assert (a != b) == False

# Task 6
def test_fraction_from_int():
    a = Fraction(1)
    b = Fraction('2')
    c, d = map(Fraction.reverse, (a + 2, b - 1))
    print(a, b, c, d)
    print(a > b, c > d)
    print(a >= 1, b >= 1, c >= 1, d >= 1)

def test_operation_btw_fraction_and_int():
    a = Fraction(1, 2)
    b = Fraction('2/3')
    c, d = map(Fraction.reverse, (a + 2, b - 1))
    print(a, b, c, d)
    print(a > b, c > d)
    print(a >= 1, b >= 1, c >= 1, d >= 1)

# Task 7
def test_r_opperands_funcs_1():
    a = Fraction(1)
    b = Fraction('2')
    c, d = map(Fraction.reverse, (2 + a, -1 + b))
    assert (str(a), str(b), str(c), str(d)) == ("1/1", "2/1", "1/3", "1/1")
    assert (a > b, c > d) == (False, False)
    assert (a >= 1, b >= 1, c >= 1, d >= 1) == (True, True, False, True)

def test_r_opperands_funcs_2():
    a = Fraction(1, 2)
    b = Fraction('2/3')
    c, d = map(Fraction.reverse, (3 - a, 2 / b))
    assert (str(a), str(b), str(c), str(d)) == ("1/2", "2/3", "2/5", "1/3")
    assert (a > b, c > d) == (False, True)
    assert (a >= 1, b >= 1, c >= 1, d >= 1) == (False, False, False, False)

# Additional Tests
def test_init_invalid():
    try:
        Fraction(3, 0)
    except ZeroDivisionError as e:
        pass
    else:
        assert False, "Expected ZeroDivisionError"

    try:
        Fraction("invalid_string")
    except ValueError as e:
        pass
    else:
        assert False, "Expected ValueError"

    try:
        Fraction(3.5, 2)
    except ValueError:
        assert True
    else:
        assert False, "Expected ValueError"

def test_numerator_setter():
    fraction = Fraction(3, 9)
    fraction.numerator(6)
    assert str(fraction) == "2/1"
    assert repr(fraction) in ["Fraction(2, 1)", "Fraction('2/1')"]
    try:
        fraction.numerator(3.5)
    except ValueError as e:
        pass
    else:
        assert False, "Expected ValueError"

def test_denominator_setter():
    fraction = Fraction(3, 9)
    fraction.denominator(18)
    assert str(fraction) == "1/18"
    assert repr(fraction) in ["Fraction(1, 18)", "Fraction('1/18')"]
    try:
        fraction.denominator(0)
    except ZeroDivisionError as e:
        pass
    else:
        assert False, "Expected ZeroDivisionError"

    try:
        fraction.denominator(3.5)
    except ValueError as e:
        pass
    else:
        assert False, "Expected ValueError"

def test_str_repr():
    fraction = Fraction(8, -12)
    assert str(fraction) == "-2/3"
    assert repr(fraction) in ["Fraction(-2, 3)", "Fraction('-2/3')"]

def test_positive_denominator():
    fraction = Fraction(-5, -10)
    assert str(fraction) == "1/2"
    assert repr(fraction) in ["Fraction(1, 2)", "Fraction('1/2')"]
    fraction = Fraction(5, -10)
    assert str(fraction) == "-1/2"
    assert repr(fraction) in ["Fraction(-1, 2)", "Fraction('-1/2')"]

def test_edge_cases():
    fraction = Fraction(0, 5)
    assert str(fraction) == "0/1"
    assert repr(fraction) in ["Fraction(0, 1)", "Fraction('0/1')"]

    fraction = Fraction("0/10")
    assert str(fraction) == "0/1"
    assert repr(fraction) in ["Fraction(0, 1)", "Fraction('0/1')"]

    fraction = Fraction(1, 1)
    assert str(fraction) == "1/1"
    assert repr(fraction) in ["Fraction(1, 1)", "Fraction('1/1')"]

def test_add_fractions():
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 3)
    result = f1 + f2
    assert result.numerator() == 5
    assert result.denominator() == 6

def test_add_fraction_and_integer():
    f1 = Fraction(1, 2)
    result = f1 + 1
    assert result.numerator() == 3
    assert result.denominator() == 2

def test_iadd_fractions():
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 3)
    f1 += f2
    assert f1.numerator() == 5
    assert f1.denominator() == 6

def test_iadd_fraction_and_integer():
    f1 = Fraction(1, 2)
    f1 += 1
    assert f1.numerator() == 3
    assert f1.denominator() == 2

def test_sub_fractions():
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 3)
    result = f1 - f2
    assert result.numerator() == 1
    assert result.denominator() == 6

def test_sub_fraction_and_integer():
    f1 = Fraction(3, 2)
    result = f1 - 1
    assert result.numerator() == 1
    assert result.denominator() == 2

def test_isub_fractions():
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 3)
    f1 -= f2
    assert f1.numerator() == 1
    assert f1.denominator() == 6

def test_isub_fraction_and_integer():
    f1 = Fraction(3, 2)
    f1 -= 1
    assert f1.numerator() == 1
    assert f1.denominator() == 2

def test_addition_with_fraction():
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 3)
    assert str(f1 + f2) == "5/6"
    assert str(f2 + f1) == "5/6"

def test_addition_with_int():
    f1 = Fraction(1, 2)
    assert str(f1 + 1) == "3/2"
    assert str(1 + f1) == "3/2"

def test_inplace_addition():
    f1 = Fraction(1, 2)
    f1 += Fraction(1, 3)
    assert str(f1) == "5/6"
    f1 += 1
    assert str(f1) == "11/6"

def test_subtraction_with_fraction():
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 3)
    assert str(f1 - f2) == "1/6"
    assert str(f2 - f1) == "-1/6"

def test_subtraction_with_int():
    f1 = Fraction(1, 2)
    assert str(f1 - 1) == "-1/2"
    assert str(1 - f1) == "1/2"

def test_inplace_subtraction():
    f1 = Fraction(1, 2)
    f1 -= Fraction(1, 3)
    assert str(f1) == "1/6"
    f1 -= 1
    assert str(f1) == "-5/6"

def test_multiplication_with_fraction():
    f1 = Fraction(1, 2)
    f2 = Fraction(2, 3)
    assert str(f1 * f2) == "1/3"
    assert str(f2 * f1) == "1/3"

def test_multiplication_with_int():
    f1 = Fraction(1, 2)
    assert str(f1 * 3) == "3/2"
    assert str(3 * f1) == "3/2"

def test_inplace_multiplication():
    f1 = Fraction(1, 2)
    f1 *= Fraction(2, 3)
    assert str(f1) == "1/3"
    f1 *= 3
    assert str(f1) == "1/1"

def test_division_with_fraction():
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 3)
    assert str(f1 / f2) == "3/2"
    assert str(f2 / f1) == "2/3"

def test_division_with_int():
    f1 = Fraction(1, 2)
    assert str(f1 / 2) == "1/4"
    assert str(2 / f1) == "4/1"

def test_inplace_division():
    f1 = Fraction(1, 2)
    f1 /= Fraction(1, 3)
    assert str(f1) == "3/2"
    f1 /= 3
    assert str(f1) == "1/2"

def test_addition_with_negative_fractions():
    f1 = Fraction(-1, 2)
    f2 = Fraction(1, 3)
    assert str(f1 + f2) == "-1/6"
    assert str(f2 + f1) == "-1/6"

    f3 = Fraction(-1, 3)
    assert str(f1 + f3) == "-5/6"

def test_addition_with_negative_int():
    f1 = Fraction(1, 2)
    assert str(f1 + (-1)) == "-1/2"
    assert str((-1) + f1) == "-1/2"

def test_subtraction_with_negative_fractions():
    f1 = Fraction(-1, 2)
    f2 = Fraction(1, 3)
    assert str(f1 - f2) == "-5/6"
    assert str(f2 - f1) == "5/6"

    f3 = Fraction(-1, 3)
    assert str(f1 - f3) == "-1/6"

def test_subtraction_with_negative_int():
    f1 = Fraction(1, 2)
    assert str(f1 - (-1)) == "3/2"
    assert str((-1) - f1) == "-3/2"

def test_multiplication_with_negative_fractions():
    f1 = Fraction(-1, 2)
    f2 = Fraction(1, 3)
    assert str(f1 * f2) == "-1/6"
    assert str(f2 * f1) == "-1/6"

    f3 = Fraction(-1, 3)
    assert str(f1 * f3) == "1/6"

def test_multiplication_with_negative_int():
    f1 = Fraction(1, 2)
    assert str(f1 * (-3)) == "-3/2"
    assert str((-3) * f1) == "-3/2"

def test_division_with_negative_fractions():
    f1 = Fraction(-1, 2)
    f2 = Fraction(1, 3)
    assert str(f1 / f2) == "-3/2"
    assert str(f2 / f1) == "-2/3"

    f3 = Fraction(-1, 3)
    assert str(f1 / f3) == "3/2"

def test_division_with_negative_int():
    f1 = Fraction(1, 2)
    assert str(f1 / (-2)) == "-1/4"
    assert str((-2) / f1) == "-4/1"

def test_inplace_operations_with_negative_fractions():
    f1 = Fraction(-1, 2)
    f2 = Fraction(1, 3)

    f1 += f2
    assert str(f1) == "-1/6"

    f1 -= f2
    assert str(f1) == "-1/2"

    f1 *= f2
    assert str(f1) == "-1/6"

    f1 /= f2
    assert str(f1) == "-1/2"

def test_all_operations_combined():
    # 1. Fraction первым аргументом
    f1 = Fraction(1, 2)  # Положительная дробь
    f2 = Fraction(-2, 3)  # Отрицательная дробь

    assert str(f1 + f2) == "-1/6"
    assert str(f1 - f2) == "7/6"
    assert str(f1 * f2) == "-1/3"
    assert str(f1 / f2) == "-3/4"

    # 2. Fraction вторым аргументом
    assert str(f2 + f1) == "-1/6"
    assert str(f2 - f1) == "-7/6"
    assert str(f2 * f1) == "-1/3"
    assert str(f2 / f1) == "-4/3"

    # 3. Операции с int
    i = -3
    assert str(f1 + i) == "-5/2"
    assert str(i + f1) == "-5/2"
    assert str(f1 - i) == "7/2"
    assert str(i - f1) == "-7/2"
    assert str(f1 * i) == "-3/2"
    assert str(i * f1) == "-3/2"
    assert str(f1 / i) == "-1/6"
    assert str(i / f1) == "-6/1"

    # 4. Переход через 0 (например, дробь приближается к 0)
    f3 = Fraction(1, 3)  # Положительная дробь
    f4 = Fraction(-1, 3)  # Отрицательная дробь

    assert str(f3 + f4) == "0/1"
    assert str(f3 - f4) == "2/3"
    assert str(f3 * f4) == "-1/9"
    assert str(f3 / f4) == "-1/1"

def test_all_operations_combined_with_zero():
    # 1. Fraction первым аргументом
    f1 = Fraction(1, 2)  # Положительная дробь
    f2 = Fraction(0)  # Отрицательная дробь

    assert str(f1 + f2) == "1/2"
    assert str(f1 - f2) == "1/2"
    assert str(f1 * f2) == "0/1"
    try:
        Fraction(3, 0)
    except ZeroDivisionError as e:
        pass
    else:
        assert False, "Expected ZeroDivisionError"

    # 2. Fraction вторым аргументом
    assert str(f2 + f1) == "1/2"
    assert str(f2 - f1) == "-1/2"
    assert str(f2 * f1) == "0/1"
    assert str(f2 / f1) == "0/1"

    # 3. Операции с int
    i = -14
    assert str(f2 + i) == f"{i}/1"
    assert str(i + f2) == f"{i}/1"
    assert str(f2 - i) == f"{-i}/1"
    assert str(i - f2) == f"{i}/1"
    assert str(f2 * i) == "0/1"
    assert str(i * f2) == "0/1"
    assert str(f2 / i) == "0/1"
    try:
        str(i / f2)
    except ZeroDivisionError as e:
        pass
    else:
        assert False, "Expected ZeroDivisionError"

def test_all_compound_operations():
    # Fraction и Fraction
    f1 = Fraction(1, 2)
    f2 = Fraction(-2, 3)
    
    # +=
    f1 += f2
    assert str(f1) == "-1/6"
    f1 = Fraction(1, 2)  # Сброс
    # -=
    f1 -= f2
    assert str(f1) == "7/6"
    f1 = Fraction(1, 2)  # Сброс
    # *=
    f1 *= f2
    assert str(f1) == "-1/3"
    f1 = Fraction(1, 2)  # Сброс
    # /=
    f1 /= f2
    assert str(f1) == "-3/4"

    # Fraction и int
    f1 = Fraction(1, 2)
    i = -3
    
    f1 += i
    assert str(f1) == "-5/2"
    f1 = Fraction(1, 2)  # Сброс
    
    f1 -= i
    assert str(f1) == "7/2"
    f1 = Fraction(1, 2)  # Сброс
    
    f1 *= i
    assert str(f1) == "-3/2"
    f1 = Fraction(1, 2)  # Сброс
    
    f1 /= i
    assert str(f1) == "-1/6"

    # Int и Fraction (обратные операции не поддерживают встроенные compound операторы)
    # Поэтому тестируем только корректность __radd__, __rsub__, __rmul__, __rtruediv__

    assert str(i + Fraction(1, 2)) == "-5/2"
    assert str(i - Fraction(1, 2)) == "-7/2"
    assert str(i * Fraction(1, 2)) == "-3/2"
    assert str(i / Fraction(1, 2)) == "-6/1"

    # Проверка через 0
    f3 = Fraction(1, 3)
    f4 = Fraction(-1, 3)
    f3 += f4
    assert str(f3) == "0/1"
    f3 = Fraction(1, 3)  # Сброс
    
    f3 -= f4
    assert str(f3) == "2/3"
    f3 = Fraction(1, 3)  # Сброс
    
    f3 *= f4
    assert str(f3) == "-1/9"
    f3 = Fraction(1, 3)  # Сброс
    
    f3 /= f4
    assert str(f3) == "-1/1"

def test_all_compound_operations_with_int_right():
    # Fraction и int
    f1 = Fraction(1, 2)
    i = -3
    
    # +=
    f1 += i
    assert str(f1) == "-5/2"
    f1 = Fraction(1, 2)  # Сброс
    
    # -=
    f1 -= i
    assert str(f1) == "7/2"
    f1 = Fraction(1, 2)  # Сброс
    
    # *=
    f1 *= i
    assert str(f1) == "-3/2"
    f1 = Fraction(1, 2)  # Сброс
    
    # /=
    f1 /= i
    assert str(f1) == "-1/6"

    # Дополнительные проверки с другими числами
    f2 = Fraction(-2, 3)
    j = 4
    
    f2 += j
    assert str(f2) == "10/3"
    f2 = Fraction(-2, 3)  # Сброс
    
    f2 -= j
    assert str(f2) == "-14/3"
    f2 = Fraction(-2, 3)  # Сброс
    
    f2 *= j
    assert str(f2) == "-8/3"
    f2 = Fraction(-2, 3)  # Сброс
    
    f2 /= j
    assert str(f2) == "-1/6"

    # Проверка с нулём и дробью
    f3 = Fraction(1, 3)
    k = 0  # Проверка нейтрального элемента сложения
    f3 += k
    assert str(f3) == "1/3"
    f3 -= k
    assert str(f3) == "1/3"
    
    # Умножение на 0 (результат — 0)
    f3 *= k
    assert str(f3) == "0/1"
    f3 = Fraction(1, 3)  # Сброс

    # Деление на 1 (должно остаться неизменным)
    f3 /= 1
    assert str(f3) == "1/3"

def test_fraction_comparisons():
    # Fraction и Fraction
    f1 = Fraction(1, 2)
    f2 = Fraction(2, 4)  # Эквивалентно f1
    f3 = Fraction(3, 4)

    assert f1 == f2
    assert f1 != f3
    assert f1 < f3
    assert f1 <= f3
    assert f3 > f1
    assert f3 >= f1

    # Проверка с отрицательными значениями
    f4 = Fraction(-1, 2)
    f5 = Fraction(-3, 4)
    
    assert f4 < f1
    assert f4 != f5
    assert f4 > f5
    assert f5 <= f4

def test_fraction_int_comparisons():
    # Fraction и int
    f1 = Fraction(1, 2)
    f2 = Fraction(-3, 2)
    i1 = 1
    i2 = -2

    # Положительная дробь и целое число
    assert f1 < i1
    assert f1 <= i1
    assert f1 != i1
    assert i1 > f1
    assert i1 >= f1

    # Отрицательная дробь и целое число
    assert f2 < i1
    assert (f2 < i2) == False
    assert f2 != i2
    assert (i2 > f2) == False
    assert (i2 >= f2) == False

def test_int_fraction_comparisons():
    # Int и Fraction
    f1 = Fraction(3, 2)
    f2 = Fraction(-1, 3)
    i1 = 2
    i2 = 0

    # Положительное целое и дробь
    assert i1 > f1
    assert i1 >= f1
    assert i1 != f1
    assert f1 < i1
    assert f1 <= i1

    # Ноль и отрицательная дробь
    assert i2 > f2
    assert i2 >= f2
    assert i2 != f2
    assert f2 < i2
    assert f2 <= i2
