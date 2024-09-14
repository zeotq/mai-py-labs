def broken_sum(a: int, b: int) -> int:
    a_1 = a // 100
    a_2 = a // 10 - a_1 * 10
    a_3 = a % 10
    b_1 = b // 100
    b_2 = b // 10 - b_1 * 10
    b_3 = b % 10
    c_1 = (a_1 + b_1) % 10
    c_2 = (a_2 + b_2) % 10
    c_3 = (a_3 + b_3) % 10

    return c_1 * 100 + c_2 * 10 + c_3
    

n_1, n_2 = [int(input()) for i in range(2)]
print(broken_sum(n_1, n_2))