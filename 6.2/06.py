import pandas as pd


def best(data_frame: pd.DataFrame):
    """Returns the best students of group / Wrong

    Args:
        data_frame (pd.DataFrame): ...

    Returns:
        pd.DataFrame: only the best students
    """
    copy_frame = data_frame.copy()
    copy_frame['sum'] = copy_frame['maths'] + copy_frame['physics'] + copy_frame['computer science']
    copy_frame.sort_values(['sum'], ascending=True, inplace=True)
    copy_frame = copy_frame[copy_frame['sum'] == max(copy_frame['sum'])]
    copy_frame.drop(columns=['sum'], inplace=True)
    return copy_frame


def best(journal: pd.DataFrame) -> pd.DataFrame:
    """Find all students who have all marks greater than or equal to 4

    Args:
        journal (pd.DataFrame): ...

    Returns:
        pd.DataFrame: students with correct marks 
    """
    filtered_journal = journal[
        (journal['maths'] >= 4) & 
        (journal['physics'] >= 4) & 
        (journal['computer science'] >= 4)
    ]
    return filtered_journal


def test_1():
    columns = ['name', 'maths', 'physics', 'computer science']
    data = {
        'name': ['Иванов', 'Петров', 'Сидоров', 'Васечкин', 'Николаев'],
        'maths': [5, 4, 5, 2, 4],
        'physics': [4, 4, 4, 5, 5],
        'computer science': [5, 2, 5, 4, 3]
    }
    journal = pd.DataFrame(data, columns=columns)
    filtered = best(journal)
    print(journal)
    print(filtered)


if __name__ == "__main__":
    test_1()