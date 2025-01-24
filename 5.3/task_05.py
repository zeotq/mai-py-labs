def checking_the_order(iterable_obj) -> bool:
    old = float("-inf")
    for i in iterable_obj:
        if old > i:
            return False
        old = i
    return True


def merge(n: tuple, m: tuple) -> tuple:
    try:
        iter(n)
        iter(m)
    except Exception:
        raise StopIteration
    
    if (any(type(x) is not type(n[0]) for x in n) or 
            any(type(x) is not type(m[0]) for x in m) or
            type(n[0]) is not type(m[0])):
        raise TypeError
    
    if not checking_the_order(n) or not checking_the_order(m):
        raise ValueError

    len_n, len_m = len(n), len(m)
    i, j = 0, 0
    result = [0] * (len_n + len_m)
    while (i + j) < (len_n + len_m):
        x = float('inf') if i >= len_n else n[i]
        y = float('inf') if j >= len_m else m[j]
        if x > y:
            result[i + j] = y
            j += 1
        else:
            result[i + j] = x
            i += 1

    return tuple(result)


def main():
    # Value Error
    print(*merge([3, 2, 1], range(10)))


if __name__ == "__main__":
    main()