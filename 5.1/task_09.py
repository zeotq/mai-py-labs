class Queue:
    def __init__(self):
        self.q = list()

    def is_empty(self):
        return len(self.q) == 0
    
    def push(self, item):
        self.q.append(item)

    def pop(self):
        return self.q.pop(0)


def main():
    queue = Queue()
    for item in range(10):
        queue.push(item)
    while not queue.is_empty():
        print(queue.pop(), end=" ")


if __name__ == "__main__":
    main()