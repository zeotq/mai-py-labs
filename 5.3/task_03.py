def func(a, b, c):
    return ''.join(map(str, (a, b, c)))


class Killer:
    def __str__(self):
        raise StopAsyncIteration("Ура! Ошибка!")
    
    def __repr__(self):
        raise StopAsyncIteration("Ура! Ошибка!")


def main():
    args = Killer()
    try:
        func(args)
    except Exception:
        print("Ура! Ошибка!")
    else:
        print("No Exceptions")


if __name__ == "__main__":
    main()
