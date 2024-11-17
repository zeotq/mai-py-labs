from itertools import product


def main():
    source_function = input()
    custom_vars_to_vars = dict((i, None) for i in source_function if i.isupper())
    variable_names = list(custom_vars_to_vars.keys())
    print(*variable_names, "F")

    for values in reversed(list(product([1, 0], repeat=len(variable_names)))):
        current_vars = dict(zip(variable_names, values))
        try:
            result = eval(source_function, {}, current_vars)
            print(*values, int(result))
        except Exception as e:
            print("Всё пошло по пизде: ", e)
            return


if __name__ == "__main__":
    main()