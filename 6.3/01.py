import requests


object = requests.get("http://127.0.0.1:5000")
decoded_content = object.content.decode()
print(decoded_content)
