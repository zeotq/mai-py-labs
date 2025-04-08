from datetime import datetime


class Comment(object):
    def __init__(self, name: str, date: str, text: str):
        self.name = name
        self.date = datetime.strptime(date, '%d-%m-%Y %H:%M')
        self.text = text

    def get_author(self) -> str:
        return self.name

    def get_date(self) -> str:
        return self.date.strftime('%d-%m-%Y')

    def get_time(self) -> str:
        return self.date.strftime('%H:%M')

    def get_text(self) -> str:
        return self.text

def test_1():
    a = Comment('Вася', '23-02-2023 12:43', 'первый')
    print(a.get_author())
    print(a.get_date())
    print(a.get_time())
    print(a.get_text())

if __name__ == "__main__":
    test_1()