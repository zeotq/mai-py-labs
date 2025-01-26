from requests import put
from json import dumps
from sys import stdin


def put_request_to_server(address: str = "http://127.0.0.1:5000", user_id: int = None, user_data: dict = None):
    """Send get request to server

    Args:
        addres (str): server addres. Defaults to http://127.0.0.1:5000. 
    """
    if "http://" not in address:
        address = f'http://{address}'

    responce = put(f"{address}/users/{user_id}", dumps(user_data))
    

def main():
    address = input()
    user_id = int(input())
    new_data = dict()
    for i in stdin:
        u_key, u_data = i.rstrip("\n").split("=")
        new_data[u_key] = u_data
    put_request_to_server(address, user_id, new_data)
    

if __name__ == "__main__":
    main()