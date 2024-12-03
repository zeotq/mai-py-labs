def answer(func):
    def new_func(*args, **kwargs):
        return f'Результат функции: {func(*args, **kwargs)}'
    return new_func


def main():
    @answer
    def a_plus_b(a, b):
        return a + b
    

    @answer
    def get_letters(text: str) -> str:
        return ''.join(sorted(set(filter(str.isalpha, text.lower()))))


    print(a_plus_b(3, 5))
    print(a_plus_b(7, 9))

    print(get_letters('Hello, world!'))
    print(get_letters('Декораторы это круто =)'))   


if __name__ == "__main__":
    main()