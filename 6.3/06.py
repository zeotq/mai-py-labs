from requests import get
from json import loads


def requests_to_server(address: str = "http://127.0.0.1:5000"):
    """Send get request to server

    Args:
        addres (str): server addres. Defaults to http://127.0.0.1:5000. 
    """
    if "http://" not in address:
        address = f'http://{address}'

    decoded_content = loads(get(f"{address}/users").content)
    names = sorted([f'{el['last_name']} {el['first_name']}' for el in decoded_content])

    print(*names, sep='\n')


def main():
    requests_to_server(input())


if __name__ == "__main__":
    main()