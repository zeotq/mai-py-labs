def reader():
    temp = []
    while (integer:=input()) != 'end':
        temp.append(int(integer))
    return temp
    

def average(x):
    return sum(x) / len(x)


def main():
    n = int(input())
    out = min([average(reader()) for i in range(n)])
    print(round(out, 2))


if __name__ == '__main__':
    main()