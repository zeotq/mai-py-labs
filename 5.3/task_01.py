def func():
    x = int('Hello, world!')


def main():
    try:
        func()
    except Exception as e:
        print(type(e).__name__)
    else:
        print("No Exceptions")    


if __name__ == "__main__":
    main()