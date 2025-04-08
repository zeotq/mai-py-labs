from datetime import datetime


class Comment(object):
    def __init__(self, name: str, date: str, text: str):
        self.name = name
        self.date = datetime.strptime(date, '%d-%m-%Y %H:%M')
        self.text = text
        self.approved = False
        self.edited = False

    def get_author(self) -> str:
        return self.name

    def get_date(self) -> str:
        return self.date.strftime('%d-%m-%Y')

    def get_time(self) -> str:
        return self.date.strftime('%H:%M')

    def get_text(self) -> str:
        return self.text
    
    def approve(self) -> None:
        self.approved = True
    
    def is_approved(self) -> bool:
        return self.approved
    
    def set_text(self, text: str) -> None:
        self.approved = False
        self.edited = True
        self.text = text

    def is_edited(self) -> bool:
        return self.edited
    
    def __str__(self):
        return self.text + '\n' + f'[{self.name} ({self.date.strftime('%d-%m-%Y %H:%M')})]' + '\n'


def test_2():
    a = Comment('Вася', '23-02-2023 12:43', 'первый')
    print(a)
    print(a.is_approved(), a.is_edited())
    a.approve()
    a.set_text('Первый!!!')
    print(a.is_approved(), a.is_edited())
    a.approve()
    print(a.is_approved(), a.is_edited())
    print(a)

if __name__ == "__main__":
    test_2()