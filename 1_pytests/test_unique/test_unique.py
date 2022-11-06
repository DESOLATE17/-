import pytest
import gen_random

class Unique(object):
    def __init__(self, items, **kwargs):
        self.seen = []
        for i in items: 
            if  len(kwargs) > 0 and kwargs["ignore_case"]:
                flag = True
                for j in self.seen:
                    if j.lower() == i.lower():
                        flag = False
                if flag:
                    (self.seen).append(i)   
            else:
                if i in self.seen:
                    continue
                self.seen.append(i)    

    def __next__(self):
        if len(self.seen) == 0:
            raise StopIteration
        item = self.seen[0]
        del self.seen[0]
        return item

    def __iter__(self):
        return self

@pytest.fixture
def data():
    d = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    return d

def test_unique_ignore_case_True(data):
    t = list(Unique(data, ignore_case = True))
    res = ['a', 'b']
    assert res == t

def test_unique_ignore_case_False(data):
    t = list(Unique(data))
    res = ['a', 'A', 'b', 'B']
    assert res == t

def test_unique_numbers():
    data = [1,1,1,1,1,1,2,2,2,2,2,2]
    t = list(Unique(data))
    res = [1, 2]
    assert res == t

