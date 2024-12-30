class Checkers:
    def __init__(self):
        self.matrix = [[Cell("X") for _ in range(8)] for _ in range(8)]
        for i in range(0, 3):
            if (i % 2) == 1: 
                for j in range(0, 8, 2):
                    self.matrix[i][j] = Cell("B")
                    self.matrix[7 - i][j + 1] = Cell("W")
            else:
                for j in range(1, 8, 2):
                    self.matrix[i][j] = Cell("B")
                    self.matrix[7 - i][j - 1] = Cell("W")

    def get_cell(self, adr: str = "A1"):
        col = 8 - int(adr[1::])
        row = ord(adr[0]) - ord('A')
        return self.matrix[col][row]

    def move(self, old, new):
        col = 8 - int(old[1::])
        row = ord(old[0]) - ord('A')
        col_new = 8 - int(new[1::])
        row_new = ord(new[0]) - ord('A')
        self.matrix[col_new][row_new] = self.matrix[col][row]
        self.matrix[col][row] = Cell("X")


class Cell:
    def __init__(self, status):
        self.stat = status

    def status(self):
        return self.stat   
    

def main():
    checkers = Checkers()
    checkers.move('C3', 'D4')
    checkers.move('H6', 'G5')
    for row in '87654321':
        for col in 'ABCDEFGH':
            print(checkers.get_cell(col + row).status(), end='')
        print()


if __name__ == '__main__':
    main()