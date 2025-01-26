import pandas as pd


def update(journal: pd.DataFrame) -> pd.DataFrame:
    """Add average mark, sort in descending order by average mark

    Args:
        journal (pd.DataFrame): ...

    Returns:
        pd.DataFrame: new frame
    """
    copy_frame = journal.copy()
    copy_frame['average'] = (copy_frame['maths'] + copy_frame['physics'] + copy_frame['computer science']) / 3
    copy_frame.sort_values(by=['average', 'name'], ascending=[False, True], inplace=True)
    return copy_frame


def test_1():
    columns = ['name', 'maths', 'physics', 'computer science']
    data = {
        'name': ['Иванов', 'Петров', 'Сидоров', 'Васечкин', 'Николаев'],
        'maths': [5, 4, 5, 2, 4],
        'physics': [4, 4, 4, 5, 5],
        'computer science': [5, 2, 5, 4, 3]
    }
    journal = pd.DataFrame(data, columns=columns)
    filtered = update(journal)
    print(journal)
    print(filtered)


if __name__ == "__main__":
    test_1()