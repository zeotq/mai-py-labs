def rabbit_8(data: list = [[]]) -> set:
    """Return the set of double demmension list

    Args:
        data (list): double demmension list 

    Returns:
        set(): 
    """
    out = set()
    for x in data:
        for y in x:
            out.add(y)
    return out


def main():
    print('\n'.join(list(rabbit_8([input().split() for i in range(int(input()))]))))


if __name__ == "__main__":
    main()
