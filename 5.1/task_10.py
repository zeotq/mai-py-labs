class Stack:
    def __init__(self):
        self.q = list()

    def is_empty(self):
        return len(self.q) == 0
    
    def push(self, item):
        self.q.append(item)

    def pop(self):
        return self.q.pop(-1)


def main():
    stack = Stack()
    for item in range(10):
        stack.push(item)
    while not stack.is_empty():
        print(stack.pop(), end=" ")


if __name__ == "__main__":
    main()