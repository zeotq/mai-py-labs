from requests import get
from json import loads
from sys import stdin


def requests_to_server(address: str = "http://127.0.0.1:5000"):
    """Send get request to server

    Args:
        addres (str): server addres. Defaults to http://127.0.0.1:5000. 
    """
    if "http://" not in address:
        address = f'http://{address}'

    result = 0

    for i in stdin:
        decoded_content = loads(get(f"{address}{i.strip('\n')}").content)
        temp_s = sum(filter(lambda a: isinstance(a, int), decoded_content))
        if temp_s is not None:
            result += temp_s

    print(result)


def main():
    requests_to_server(input())


if __name__ == "__main__":
    main()