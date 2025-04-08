from datetime import datetime


class Comment(object):
    def __init__(self, name: str, date: str, text: str):
        self.name = name
        self._date = datetime.strptime(date, '%d-%m-%Y %H:%M')
        self._text = text
        self._is_approved = False
        self._is_edited = False
        self._sub_comments = []

    def get_author(self) -> str:
        return self.name

    def get_date(self) -> str:
        return self._date.strftime('%d-%m-%Y')

    def get_time(self) -> str:
        return self._date.strftime('%H:%M')

    def get_text(self) -> str:
        return self._text
    
    def approve(self) -> None:
        self._is_approved = True
    
    def is_approved(self) -> bool:
        return self._is_approved
    
    def set_text(self, text: str) -> None:
        self._is_approved = False
        self._is_edited = True
        self._text = text

    def is_edited(self) -> bool:
        return self._is_edited
    
    def get_sub_comments(self):
        return self._sub_comments
    
    def __iadd__(self, sub_comment):
        if isinstance(sub_comment, SubComment):
            sub_comment.set_parent(self)
        return self

    def __contains__(self, other):
        if other in self._sub_comments:
            return True
        return any(other in sub for sub in self._sub_comments)
    
    def __lt__(self, other):
        return other in self

    def __gt__(self, other):
        return self in other
    
    def __repr__(self):
        return f'Comment({self.name}, {self.get_date()}, {self.get_time()})'
    
    def __str__(self):
        return self._text + '\n' + f'[{self.name} ({self._date.strftime('%d-%m-%Y %H:%M')})]' + '\n'


class SubComment(Comment):
    def __init__(self, name: str, date: str, text: str, parent=None):
        super().__init__(name, date, text)
        self.parent = None
        if parent:
            self.set_parent(parent)

    def get_parent(self):
        return self.parent

    def set_parent(self, parent):
        if isinstance(parent, Comment):
            if self.parent and self in self.parent._sub_comments:
                self.parent._sub_comments.remove(self)
            self.parent = parent
            parent._sub_comments.append(self)

    def __repr__(self):
        parent_repr = repr(self.parent) if self.parent else 'None'
        return f'SubComment({self.name}, {self.get_date()}, {self.get_time()}, {parent_repr})'


def test_3():
    a = Comment('Вася', '23-02-2023 12:43', 'первый')
    print(repr(a))
    b = SubComment('Миша', '23-02-2023 12:44', 'второй', parent=a)
    print(a.get_sub_comments())
    print(a < b, a > b, b < a, b > a)
    c = SubComment('Петя', '23-02-2023 12:54', 'третий')
    print(repr(c))
    b += c
    print(a < b, a < c, b < c, c > a)
    print(repr(c))
    c.set_parent(a)
    print(a < b, a < c, b < c, c > a)
    print(*map(repr, a.get_sub_comments()), sep='\n')

if __name__ == "__main__":
    test_3()