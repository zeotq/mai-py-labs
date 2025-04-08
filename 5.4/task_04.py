from datetime import datetime


class ParentRecursionError(RecursionError):
    ...


class ParentTypeError(TypeError):
    ...


class Comment(object):
    def __init__(self, name: str, date: str, text: str):
        if not isinstance(name, str):
            raise TypeError
        if not isinstance(date, str):
            raise TypeError
        if not isinstance(text, str):
            raise TypeError

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
        if not isinstance(text, str):
            raise TypeError

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
        else:
            raise ParentTypeError
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
        if not (isinstance(parent, Comment) or parent is None):
            raise ParentTypeError
        self.parent = None
        if parent:
            self.set_parent(parent)

    def get_parent(self):
        return self.parent

    def set_parent(self, parent):
        if isinstance(parent, Comment):
            if self < parent:
                raise ParentRecursionError

            if self.parent and self in self.parent._sub_comments:
                self.parent._sub_comments.remove(self)
            self.parent = parent
            parent._sub_comments.append(self)
        else:
            raise ParentTypeError

    def __repr__(self):
        parent_repr = repr(self.parent) if self.parent else 'None'
        return f'SubComment({self.name}, {self.get_date()}, {self.get_time()}, {parent_repr})'


def test_4():
    try:
        a = Comment(123, 123, 123)
    except TypeError:
        print('TypeError raised')

    try:
        a = SubComment('user', 'hello', 'hello')
    except ValueError:
        print('ValueError raised')

    try:
        a = SubComment('first', '01-05-2023 00:00', 'hello')
        b = SubComment('second', '01-05-2023 00:00', 'hello', parent=a)
        a.set_parent(b)
        print(a.parent, b.parent)
    except ParentRecursionError:
        print('ParentRecursionError raised')

if __name__ == "__main__":
    test_4()