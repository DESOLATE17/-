import pytest
#python3 -m pytest tests
#putest test_sort.py
#pytest -rp
def my_sort1(data):
    return sorted(data, key = abs, reverse = True)

def my_sort2(data):
    return sorted(data, key = lambda n: -abs(n))

def test_my_sort1():
    data = [4, -30, 100, -100, 123, 1, 0, -1, -4]
    res = [123, 100, -100, -30, 4, -4, 1, -1, 0]
    assert res == my_sort1(data)

def test_my_sort2():
    data = [4, -30, 100, -100, 123, 1, 0, -1, -4]
    res = [123, 100, -100, -30, 4, -4, 1, -1, 0]
    assert res == my_sort2(data)