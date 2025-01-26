import pandas as pd


def need_to_work_better(journal: pd.DataFrame) -> pd.DataFrame:
    """Find all students who have any 2

    Args:
        journal (pd.DataFrame): ...

    Returns:
        pd.DataFrame: students who have to work better
    """
    filtered_journal = journal[
        (journal['maths'] == 2) |
        (journal['physics'] == 2) | 
        (journal['computer science'] == 2)
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
    filtered = need_to_work_better(journal)
    print(journal)
    print(filtered)


if __name__ == "__main__":
    test_1()