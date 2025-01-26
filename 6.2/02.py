import pandas as pd
import re


def length_stats(text: str) -> tuple[pd.Series]:
    """Create Series object with words as keys and word len values

    Args:
        text (str): any text

    Returns:
        tuple[pd.Series]: Two Series object with word len from word
        - First: odd
        - Second: even
    """

    # Normalize text
    pattern = re.compile(r'[\W\d_]', re.UNICODE)
    words = sorted(re.split(pattern, text.lower()))

    words = [word for word in words if word]
    word_lengths = {word: len(word) for word in words}
    
    # Seperating words
    odd_lengths = {word: length for word, length in word_lengths.items() if length % 2 != 0}
    even_lengths = {word: length for word, length in word_lengths.items() if length % 2 == 0}
    
    # Convert to Series
    odd_series = pd.Series(odd_lengths, dtype='int64')
    even_series = pd.Series(even_lengths, dtype='int64')
    
    return odd_series, even_series


def test_1():
    odd, even = length_stats('Мама мыла раму')
    print(odd)
    print(even)

def test_2():
    odd, even = length_stats('Лес, опушка, странный домик. Лес, опушка и зверушка.')
    print(odd)
    print(even)


if __name__ == "__main__":
    test_1()
    test_2()