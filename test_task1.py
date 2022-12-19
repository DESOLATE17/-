import pytest
from rk1_functions import Manufacturer, Detail, DetMan, task1, task2, task3

@pytest.fixture
def man():
   
    man = [
        Manufacturer(1, "Гидросталь"),
        Manufacturer(2, "Россталь"),
        Manufacturer(3, "Эргон"),
        Manufacturer(4, "Авток"),
        Manufacturer(5, "Арстат")
    ]

    return man

@pytest.fixture
def det():

    det = [
    Detail(1, "штуцер", 1, 100),
    Detail(2, "Винт", 2, 50),
    Detail(3, "Втулка", 4, 70),
    Detail(4, "Шпонка", 3, 110),
    Detail(5, "Пружина", 4, 45),
    Detail(6, "Шпонка2", 5, 40)
    ]

    return det

@pytest.fixture
def men_dets():
    men_dets = [
    DetMan(1,1),
    DetMan(2,2),
    DetMan(3,3),
    DetMan(3,4),
    DetMan(3,5),
    DetMan(4,1),
    DetMan(5,2),
    DetMan(5,3),
    DetMan(4,4),
    DetMan(6,5),
    ]
    return men_dets


def test_task1(man, det):
    assert task1(man, det) == {'Авток': ['Втулка', 'Пружина'], 'Арстат': ['Шпонка2']}

def test_task2(man, det):
    assert task2(man, det) == [('Эргон', 110), ('Гидросталь', 100), ('Авток', 70), ('Россталь', 50), ('Арстат', 40)]

def test_task3(man, det, men_dets):
    assert task3(man, det, men_dets) == [('Авток', 'Втулка', 70), ('Авток', 'Шпонка', 110), ('Арстат', 'Втулка', 70), ('Арстат', 'Шпонка2', 40), 
    ('Гидросталь', 'штуцер', 100), ('Гидросталь', 'Шпонка', 110), ('Россталь', 'Винт', 50), ('Россталь', 'Пружина', 45), ('Эргон', 'Втулка', 70), 
    ('Эргон', 'Пружина', 45)]
