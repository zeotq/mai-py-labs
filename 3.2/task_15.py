def binAnalytic(binary='0b0') -> list:
    binary = binary[2::]
    output = {
        "digits": len(binary),
        "units": binary.count("1"),
        "zeros": binary.count("0")
    }
    return output


def main():
    data = list(map(binAnalytic, (map(bin, (map(int, input().split()))))))
    print(data)

        
if __name__ == "__main__":
    main()
