import pandas as pd
import re


def length_stats(text: str) -> pd.Series:
    """Create Series object with words as keys and word len values

    Args:
        text (str): any text

    Returns:
        pd.Series: Series object with word len from word
    """

    # Normalize text
    pattern = re.compile(r'[\W\d_]', re.UNICODE)

    words = re.split(pattern, text.lower())
    words = [word for word in words if word]

    text = sorted(set(words))

    # Create data Series
    res = pd.Series([len(w) for w in text], index=text)
    return res


def test_1():
    print(length_stats('Мама мыла раму'))
    print(length_stats('Лес, опушка, странный домик. Лес, опушка и зверушка.'))


if __name__ == "__main__":
    test_1()