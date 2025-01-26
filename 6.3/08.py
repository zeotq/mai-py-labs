from requests import post
from json import dumps
from sys import stdin


def post_request_to_server(address: str = "http://127.0.0.1:5000", user_data: dict = None):
    """Send get request to server

    Args:
        addres (str): server addres. Defaults to http://127.0.0.1:5000. 
    """
    if "http://" not in address:
        address = f'http://{address}'

    responce = post(f"{address}/users", dumps(user_data))


def pack_user_data(username: str, last_name: str, first_name: str, email: str) -> str:
    data = {
        "username": username,
        "last_name": last_name,
        "first_name": first_name,
        "email": email
    }
    return data
    

def main():
    post_request_to_server(user_data=pack_user_data(*[input() for i in range(4)]))


if __name__ == "__main__":
    main()