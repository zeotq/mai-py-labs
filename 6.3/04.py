from requests import get
from json import loads


def requests_to_server(address: str = "http://127.0.0.1:5000"):
    """Send get request to server

    Args:
        addres (str): server addres. Defaults to http://127.0.0.1:5000. 
    """
    if "http://" not in address:
        address = f'http://{address}'

    object = get(address)
    decoded_content = loads(object.content)
    key = input()
    
    if type(decoded_content) is dict: 
        print(decoded_content.get(key, 'No data'))
    

def main():
    requests_to_server(input())


if __name__ == "__main__":
    main()