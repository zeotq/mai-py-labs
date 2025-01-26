import requests
from json import loads


def requests_to_server(address: str = "http://127.0.0.1:5000"):
    """Send get request to server

    Args:
        addres (str): server addres. Defaults to http://127.0.0.1:5000. 
    """
    if "http://" not in address:
        address = f'http://{address}'

    object = requests.get(address)
    decoded_content = loads(object.content)
    print(sum(filter(lambda a: isinstance(a, int), decoded_content)))


def main():
    requests_to_server(input())


if __name__ == "__main__":
    main()