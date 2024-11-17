from itertools import product


class logicOperation:
    def __init__(
            self, 
            keyname: str, 
            inputs_count: int | None = 1, 
            priority: int | None = 0, 
            func=lambda a: a):
        self.name = keyname
        self.inputs_count = inputs_count
        self.priority = priority
        self.func = func


logic_operations = {
    "not": logicOperation("not", 1, 1, lambda a: not a),
    "and": logicOperation("and", 2, 2, lambda a, b: a and b),
    "or": logicOperation("or", 2, 3, lambda a, b: a or b),
    "^": logicOperation("xor", 2, 4, lambda a, b: (a or b) and not (a and b)),
    "->": logicOperation("implication", 2, 5, lambda a, b: not a or b),
    "~": logicOperation("equivalence", 2, 6, lambda a, b: a == b),
    "|": logicOperation("Schaeffer's stroke", 2, 7, lambda a, b: not (a and b)),
    "_": logicOperation("Pier's arrow", 2, 8, lambda a, b: not (a or b))
}


class logicFunction:
    def __init__(
            self, logical_function: str | list, 
            variables: list | None = None):
        """Generate performed logic function with the correct order of execution from source function.

        Args:
            logical_function (str | list): Input some logical function with operators from logic_operations.
            variables (list | None, optional): List of variables in fuction.
            By default, it's generated automatically.
            Defaults to None.

        Raises:
            ValueError: Your logical function is uncorrect.
        """
        if type(logical_function) is str:
            logical_function = logicFunction.func_refactoring(logical_function)

        self.vars = list(sorted(set(variables 
                                    if variables is not None 
                                    else [i for i in logical_function if i.isupper()])))
        self.beauty_source = logical_function.split() if type(logical_function) is str else logical_function
        self.operations_tree = []

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

        opetations_tree = list(self.beauty_source)
        if len([i for i in opetations_tree if i in logic_operations.keys()]) > 1:
            for operation in logic_operations.keys():
                while operation in opetations_tree:
                    index = opetations_tree.index(operation)                
                    if logic_operations[operation].inputs_count == 1:
                        opetations_tree = (opetations_tree[0:index]
                                           + list(logicFunction([opetations_tree[index],
                                                                 opetations_tree[index + 1]],
                                                                variables=self.vars))
                                           + opetations_tree[(index + 2)::])
                    elif logic_operations[operation].inputs_count == 2:
                        opetations_tree = (opetations_tree[0:(index - 1)]
                                           + list(logicFunction([opetations_tree[index - 1],
                                                                 opetations_tree[index], 
                                                                 opetations_tree[index + 1]], variables=self.vars))
                                           + opetations_tree[(index + 2)::])
                    else:
                        raise ValueError("Wrong operation founded in source function")
        self.operations_tree = opetations_tree

    def __iter__(self):
        self._index = 0
        return self
    
    def __next__(self):
        if self._index < 1:
            self._index += 1
            return self
        else:
            raise StopIteration

    def __call__(self, *args):
        """Сalculate the value of the function going down the branches of the tree.

        Returns:
            *args: The values of the variables are in alphabetical order
        """
        cur_vars = {self.vars[i]: args[i] for i in range(len(self.vars))}
        operations = self.operations_tree
        operation = logicFunction.empty_operation
        res_vars = list()
        for element in operations:
            if type(element) is logicFunction:
                res_vars.append(element(*args))
            elif element in logic_operations.keys():
                operation = logic_operations[element].func
            elif element.isupper():
                res_vars.append(cur_vars[element])
            else:
                res_vars.append(element)
        return operation(*res_vars)

    def empty_operation(n):
        return n

    def func_refactoring(logical_function):
        replaces = {
            "(": " ( ",
            ")": " ) ",
            "not not": ""
        }
        for i in replaces.keys():
            logical_function = logical_function.replace(i, replaces[i])
        return logical_function
    

def main():
    calc_input = input()
    lgfunc = logicFunction(calc_input)

    print(*lgfunc.vars, "F")
    for values in reversed(list(product([1, 0], repeat=len(lgfunc.vars)))):
        print(*values, "1" if lgfunc(*values) else "0")


if __name__ == "__main__":
    main()