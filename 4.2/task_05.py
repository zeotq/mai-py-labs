def to_string(*args, sep: str = " ", end: str = "\\n"):
    return sep.join(map(str, list(args))) + end
 

def main():
    result = to_string(1, 2, 3)
    print(result)
    data = [7, 3, 1, "hello", (1, 2, 3)]
    result = to_string(*data, sep=", ", end="!")
    print(result)


if __name__ == "__main__":
    main()