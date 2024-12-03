def calculate_file_sum(filename):
    with open(filename, 'rb') as f:
        data = f.read()

        if len(data) % 2 != 0:
            raise ValueError()
        
        sum_numbers = 0
        for i in range(0, len(data), 2):
            number = int.from_bytes(data[i:i + 2], byteorder='big', signed=False)
            sum_numbers = (sum_numbers + number) & 0xFFFF 
            
        return sum_numbers


def main():
    result = calculate_file_sum('3.5/task_20_1.num')
    print(result)


if __name__ == "__main__":
    main()