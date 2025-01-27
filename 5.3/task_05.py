def is_sorted(iterable) -> bool:
    if not iterable:
        return True
    old = None
    for i in iterable:
        if old and old > i:
            return False
        old = i
    return True


def is_one_type(iterable):
    if not iterable:
        return True
    first_type = type(iterable[0])
    return all(isinstance(item, first_type) for item in iterable)


def merge(iter_1: tuple, iter_2: tuple) -> list:    
    if not hasattr(iter_1, "__iter__") or not hasattr(iter_2, "__iter__"):  # Проверка возможности итерировать
        raise StopIteration 

    if not is_one_type(iter_1) or not is_one_type(iter_2):  # Проверка идентичности типов внутри iters
        raise TypeError
    
    if iter_1 and iter_2 and (type(iter_1[0]) is not type(iter_2[0])):  # Проверка идентичности типов между iters
        raise TypeError
    
    if not is_sorted(iter_1) or not is_sorted(iter_2):  # Проверка сортированности
        raise ValueError

    len_n, len_m = len(iter_1), len(iter_2)
    i, j = 0, 0
    result = [0] * (len_n + len_m)

    while i < len_n and j < len_m:
        if iter_1[i] < iter_2[j]:
            result[i + j] = iter_1[i]
            i += 1
        else:
            result[i + j] = iter_2[j]
            j += 1

    #  В тестах есть случай для двух range объектов, не все iterable объекты поддерживают "+"
    result[i + j:] = list(iter_1[i:]) + list(iter_2[j:])

    return tuple(result)


import pytest
def test_1():  # Test StopIteration (Error)
    with pytest.raises(StopIteration):
        merge(35, (1, 2, 3))

def test_2():  # Test ValueError (unsorted list) 
    with pytest.raises(ValueError):
        merge([3, 2, 1], range(10))

def test_3():  # Test TypeError (different types in one iterable)
    with pytest.raises(TypeError):
        merge((), (1, 2.5))

def test_4(): # Test TypeError (different between two itarables)
    with pytest.raises(TypeError):
        merge(("b", "a"), (1, 2))

def test_5():  # Test for currect work with lists
    assert (merge((1, 3, 5), (2, 4, 6)) == (1, 2, 3, 4, 5, 6))

def test_6():  # Test for currect work with emptys iterable objects
    assert merge((), ()) == ()

def test_7():
    assert merge(("a", "c"), ("b", "d")) == ("a", "b", "c", "d")

def test_8():
    assert merge((0, 1, 2), (0, 1, 2, 3)) == (0, 0, 1, 1, 2, 2, 3)

def test_9():
    assert merge((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), ()) == (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

def test_10():
    assert merge(range(0, 10), range(0, 15)) == tuple(sorted(list(range(0, 10)) + list(range(0, 15))))

if __name__ == "__main__":
    test_10()