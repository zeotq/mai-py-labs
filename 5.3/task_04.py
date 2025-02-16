def only_positive_even_sum(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError
    if a < 0 or a % 2 != 0 or b < 0 or b % 2 != 0:
        raise ValueError
    return a + b


def main():
    # Test 1
    if only_positive_even_sum(4, 8) == 12:
        print("Test 1: OK")

    # Test 2
    try:
        only_positive_even_sum(4, 9)
    except ValueError:
        print("Test 2: OK")
    except Exception:
        print("Test 2: WRONG")
    else:
        print("Test 2: WRONG")        

    # Test 3
    try:
        only_positive_even_sum(-4, 2)
    except ValueError:
        print("Test 3: OK")
    except Exception:
        print("Test 3: WRONG")
    else:
        print("Test 3: WRONG")

    # Test 4
    try:
        only_positive_even_sum(0.5, 2)
    except TypeError:
        print("Test 4: OK")
    except Exception:
        print("Test 4: WRONG")
    else:
        print("Test 4: WRONG")


if __name__ == "__main__":
    main()