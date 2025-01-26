from requests import get
from json import loads
from sys import stdin


def get_request_to_server(address: str = "http://127.0.0.1:5000", user_id: int = None):
    """Send get request to server

    Args:
        addres (str): server addres. Defaults to http://127.0.0.1:5000. 
    """
    if "http://" not in address:
        address = f'http://{address}'

    answer = get(f"{address}/users/{user_id}")

    try:
        answer.raise_for_status()
    except Exception:
        return None
    
    return loads(answer.content)

    
def create_message(user_data: dict, message_template: str):
    if user_data is None:
        print("Пользователь не найден")
        return
    result = message_template.format(**user_data)
    print(result)
    

def main():
    address = input()
    user_id = int(input())
    message_template = "\n".join([i.rstrip("\n") for i in stdin])
    # address = "http://127.0.0.1:5000"
    # user_id = 2
    # message_template = """Письмо для: {email}\nЗдравствуйте, {last_name} {first_name}"""
    users_data = get_request_to_server(address, user_id)
    create_message(users_data, message_template)


if __name__ == "__main__":
    main()