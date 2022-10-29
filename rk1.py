'''
Вариант 19
Деталь Производитель
Вариант Г.
1) «Отдел» и «Сотрудник» связаны соотношением один-ко-многим. Выведите список всех отделов, у которых название начинается с буквы «А»,
 и список работающих в них сотрудников.
2) «Отдел» и «Сотрудник» связаны соотношением один-ко-многим. Выведите список отделов с максимальной зарплатой сотрудников в каждом отделе,
 отсортированный по максимальной зарплате.
3) «Отдел» и «Сотрудник» связаны соотношением многие-ко-многим. Выведите список всех связанных сотрудников и отделов, отсортированный по отделам, 
сортировка по сотрудникам произвольная. 
'''
from heapq import merge
from operator import itemgetter
 
class Detail:
    """Деталь"""
    def __init__(self, id, name, man_id, price):
        self.id = id
        self.name = name
        self.man_id = man_id
        self.price = price
 
class Manufacturer:
    """Производитель"""
    def __init__(self, id, name):
        self.id = id
        self.name = name
 
class DetMan:
    """
    'Детали производителя' для реализации 
    связи многие-ко-многим
    """
    def __init__(self, det_id, man_id):
        self.det_id = det_id
        self.man_id = man_id
 
# Производитель
man = [
    Manufacturer(1, "Гидросталь"),
    Manufacturer(2, "Россталь"),
    Manufacturer(3, "Эргон"),
    Manufacturer(4, "Авток"),
    Manufacturer(5, "Арстат")
]

# Детали

det = [
    Detail(1, "штуцер", 1, 100),
    Detail(2, "Винт", 2, 50),
    Detail(3, "Втулка", 4, 70),
    Detail(4, "Шпонка", 3, 110),
    Detail(5, "Пружина", 4, 45),
    Detail(6, "Шпонка2", 5, 40)
]

mans_dets = [
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
 
def main():
    
    one_to_many = [(d.name, m.name, d.price) 
        for m in man 
        for d in det 
        if d.man_id == m.id]
    
    
    many_to_many_temp = [(m.name, md.det_id, md.man_id) 
        for m in man
        for md in mans_dets
        if m.id == md.man_id]
    
    many_to_many = [(man_name, d.name, d.price) 
        for man_name, det_id, _ in many_to_many_temp
        for d in det if d.id == det_id]
    
 
    print('Задание Г1')
    res_1 = {}
    for i in one_to_many:
        if i[1][0] == 'А':
            if res_1.get(i[1]) == None:
                res_1[i[1]] = [i[0]]
            else: 
                res_1[i[1]].append(i[0])
    print(res_1)
   
    print('\nЗадание Г2')
    res_2 = []
    for m in man:
        det_tmp = list((m.name, d.price) for d in det if d.man_id == m.id)
        if len(det_tmp) > 0: 
            res_2. append(max(det_tmp, key = lambda i: i[1]))
    tmp = sorted(res_2, key = itemgetter(1), reverse = True)
    print(tmp)
    
    print('\nЗадание Г3')
    print(sorted(many_to_many, key = lambda i: i[0]))

if __name__ == '__main__':
    main()
