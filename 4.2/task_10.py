def secret_replace(text: str, **kwargs) -> str:
    index = {i: 0 for i in kwargs.keys()}
    for i in text:
        if i in kwargs.keys():
            text = text.replace(i, kwargs[i][index[i]], 1)
            index[i] = (index[i] + 1) % len(kwargs[i])
    return text


def main():
    result = secret_replace(
        "ABRA-KADABRA",
        A=("Z", "1", "!"),
        B=("3",),
        R=("X", "7"),
        K=("G", "H"),
        D=("0", "2"),
    )
    print(result)
    result = secret_replace("Hello, world!", l=("hi", "y"), o=("123", "z"))
    print(result)


if __name__ == "__main__":
    main()
