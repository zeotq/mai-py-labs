from http.server import BaseHTTPRequestHandler, HTTPServer
from json import dumps, loads, JSONDecodeError
import re

users = {
    1: {
        "id": 1,
        "username": "first",
        "last_name": "Петрова",
        "first_name": "Елизавета",
        "email": "e.petrova@server.none"
    },
    2: {
        "id": 2,
        "username": "second",
        "last_name": "Иванов",
        "first_name": "Василий",
        "email": "vas.ivanov@server.none"
    },
    3: {
        "id": 3,
        "username": "third",
        "last_name": "Иванов",
        "first_name": "Виктор",
        "email": "vik.ivanov@server.none"
    }
}

class ServerHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        pattern = r'^/users/(\d+)$'
        match = re.match(pattern, self.path)
        u_key = int(match.group(1))
        if match and u_key in users:
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(dumps(users[u_key]).encode())
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(dumps(None).encode())

    def do_POST(self):
        def error_response(error):
            self.send_response(400)
            self.end_headers()
            self.wfile.write(dumps({"error": f"{error}"}).encode('utf-8'))
            return

        if self.path != "/users":
            error_response("Wrong way")
            return

        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        try:
            data = loads(post_data.decode('utf-8'))
            username = data['username']
            last_name = data['last_name']
            first_name = data['first_name']
            email = data['email']

            if not username or not last_name or not first_name or not email:
                error_response("Wrong keys")
                return

            print(data)
            response = 0
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(dumps(response).encode('utf-8'))

        except JSONDecodeError:
            error_response("Invalid JSON")

    def do_PUT(self):
        content_length = int(self.headers['Content-Length'])
        put_data = self.rfile.read(content_length)

        pattern = r'^/users/(\d+)$'
        match = re.match(pattern, self.path)
        u_key = int(match.group(1))
        if match and u_key in users:
            try:
                data = loads(put_data.decode('utf-8'))
                print(u_key, data)
            except JSONDecodeError:
                return
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()     

    def do_DELETE(self):
        self.send_response_only(200)
        self.end_headers()


def run(server_class=HTTPServer, handler_class=ServerHTTPRequestHandler, port=5000):
    server_address = ('localhost', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd server on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()