import requests


nums_accumulator = []


def accumulated_nums_sum(n: int):
    """Accumulate nums in global list and return sum of them

    Args:
        n (int, optional): nums to input. Defaults to 0.
    """
    if (n != 0):
        nums_accumulator.append(n)
        return
    return sum(nums_accumulator)


def requests_to_server(address: str = "http://127.0.0.1:5000"):
    """Send requests while server return not 0 int values

    Args:
        addres (str): server addres. Defaults to http://127.0.0.1:5000. 
    """
    if "http://" not in address:
        address = f'http://{address}'

    while True:
        object = requests.get(address)
        decoded_content = object.content.decode()
        if not decoded_content.lstrip("-").isdecimal():
            continue
    
        n = int(decoded_content)
        if n == 0:
            break
        accumulated_nums_sum(n)

    print(accumulated_nums_sum(0))


def main():
    requests_to_server(input())


if __name__ == "__main__":
    main()