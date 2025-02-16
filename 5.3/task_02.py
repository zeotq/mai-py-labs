def func(a, b):
    return a + b


def main():
    args = (map(lambda a: a[0], ["brain"]), filter(lambda b: b != map, "fuck"))
    try:
        func(*args)
    except Exception:
        print("Ура! Ошибка!")
    else:
        print("No Exceptions")    


if __name__ == "__main__":
    main()