def result_accumulator(func):
    queue = []

    def new_func(*args, method: str | None = "accumulate", **kwargs):
        queue.append(func(*args, **kwargs))
        if method == "drop":
            res = list(queue)
            queue.clear()
            return res
        return
    
    return new_func


def main():
    @result_accumulator
    def a_plus_b(a, b):
        return a + b
    

    @result_accumulator
    def get_letters(text: str) -> str:
        return ''.join(sorted(set(filter(str.isalpha, text.lower()))))


    print(a_plus_b(3, 5, method="accumulate"))
    print(a_plus_b(7, 9))
    print(a_plus_b(-3, 5, method="drop"))
    print(a_plus_b(1, -7))
    print(a_plus_b(10, 35, method="drop"))

    print(get_letters('Hello, world!'))
    print(get_letters('Декораторы это круто =)'))
    print(get_letters('Ехали медведи на велосипеде', method='drop'))


if __name__ == "__main__":
    main()