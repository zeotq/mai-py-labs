from itertools import product


class logicOperation:
    def __init__(
            self, 
            key: str, 
            inputs_count: int | None = 1, 
            priority: int | None = 0, 
            func=lambda a: 0):
        self.name = key
        self.inputs_count = inputs_count
        self.priority = priority
        self.func = func

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < 1:
            self._index += 1
            return self
        else:
            raise StopIteration

    def __str__(self):
        return self.name


log_ops = {
    "not": logicOperation("not", 1, 1, lambda a: not a),
    "and": logicOperation("and", 2, 2, lambda a, b: a and b),
    "or": logicOperation("or", 2, 3, lambda a, b: a or b),
    "^": logicOperation("xor", 2, 4, lambda a, b: (a or b) and not (a and b)),
    "->": logicOperation("implication", 2, 5, lambda a, b: not a or b),
    "~": logicOperation("equivalence", 2, 6, lambda a, b: a == b)
}


class logicFunction:
    def __init__(
            self, func_source: str | list | None = "A and not A", 
            variables: list | None = None):

        if type(func_source) is str:
            func_source = logicFunction.funcRefactoring(func_source)

        self.vars = list(sorted(set(variables if variables is not None else [i for i in func_source if i.isupper()])))
        self.beauty_source = func_source.split() if type(func_source) is str else func_source
        self.operations = []

        while "(" in self.beauty_source:
            count = 0
            start_index, stop_index = -1, -1
            temp = list()
            for index, element in enumerate(self.beauty_source):
                match element:
                    case "(":
                        if count > 0:
                            temp.append(element)
                        else:
                            start_index = index
                            temp.clear()
                        count += 1
                    case ")":
                        if count > 0:
                            count -= 1
                        if count == 0:
                            stop_index = index
                            break
                        temp.append(element)
                    case _:
                        temp.append(element)

            if start_index == -1 or stop_index == -1:
                raise ValueError("Incorrect brackets in source logical function")

            self.beauty_source = (self.beauty_source[0:start_index]
                                  + list(logicFunction(temp, variables=self.vars),)
                                  + self.beauty_source[(stop_index + 1)::])

        stack = list(self.beauty_source)

        if len([i for i in log_ops.keys() if i in stack]) > 1:
            for operation in log_ops.keys():
                while operation in stack:
                    index = stack.index(operation)                
                    if log_ops[operation].inputs_count == 1:
                        stack = (stack[0:index]
                                 + list(logicFunction([stack[index], stack[index + 1]], variables=self.vars))
                                 + stack[(index + 2)::])
                    elif log_ops[operation].inputs_count == 2:
                        stack = (stack[0:(index - 1)]
                                 + list(logicFunction([stack[index - 1], stack[index], stack[index + 1]], 
                                                      variables=self.vars))
                                 + stack[(index + 2)::])
                    else:
                        raise ValueError("Wrong operation")
        self.operations = stack

    def __iter__(self):
        self._index = 0
        return self
    
    def __next__(self):
        if self._index < 1:
            self._index += 1
            return self
        else:
            raise StopIteration

    def __str__(self):
        return self.beauty_source
        
    def empty_operation(n):
        return n

    def calcWithValues(self, *args):
        cur_vars = {self.vars[i]: args[i] for i in range(len(self.vars))}
        operations = self.operations
        operation = logicFunction.empty_operation
        res_vars = list()
        for element in operations:
            if type(element) is logicFunction:
                res_vars.append(element.calcWithValues(*args))
            elif element in log_ops.keys():
                operation = log_ops[element].func
            elif element.isupper():
                res_vars.append(cur_vars[element])
            else:
                res_vars.append(element)
        return operation(*res_vars)

    def funcRefactoring(func_source):
        replaces = {
            "(": " ( ",
            ")": " ) ",
            "not not": ""
        }
        for i in replaces.keys():
            func_source = func_source.replace(i, replaces[i])
        return func_source
    

def main():
    calc_input = input()
    func = logicFunction(calc_input)
    variables = func.vars

    print(*variables, "F")
    for values in reversed(list(product([1, 0], repeat=len(variables)))):
        print(*values, "1" if func.calcWithValues(*values) else "0")


if __name__ == "__main__":
    main()