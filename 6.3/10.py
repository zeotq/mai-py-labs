from requests import delete


def del_request_to_server(address: str = "http://127.0.0.1:5000", user_id: int = None):
    """Send get request to server

    Args:
        addres (str): server addres. Defaults to http://127.0.0.1:5000. 
    """
    if "http://" not in address:
        address = f'http://{address}'

    responce = delete(f"{address}/users/{user_id}")
    

def main():
    address = input()
    user_id = int(input())
    del_request_to_server(address, user_id)
    

if __name__ == "__main__":
    main()