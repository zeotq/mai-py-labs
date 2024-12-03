def same_type(func):

    def new_func(*args):
        if all([type(i) is type(args[0]) for i in args]):
            return func(*args)
        print("Обнаружены различные типы данных")
    
    return new_func



def main():
    @same_type
    def a_plus_b(a, b):
        return a + b
    
    @same_type
    def combine_text(*words):
        return ' '.join(words)
    

    print(a_plus_b(3, 5.2) or 'Fail')
    print(a_plus_b(7, '9') or 'Fail')
    print(a_plus_b(-3, 5) or 'Fail')

    print(combine_text('Hello,', 'world!') or 'Fail')
    print(combine_text(2, '+', 2, '=', 4) or 'Fail')
    print(combine_text('Список из 30', 0, 'можно получить так', [0] * 30) or 'Fail')


if __name__ == "__main__":
    main()