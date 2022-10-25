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
    '''
    def __init__(self, id, fio, sal, dep_id):
        self.id = id
        self.fio = fio
        self.sal = sal
        self.dep_id = dep_id
    '''
    def __init__(self, id, name, man_id):
        self.id = id
        self.name = name
        self.man_id = man_id
 
class Manufacturer:
    """Производитель"""
    '''def __init__(self, id, name):
        self.id = id
        self.name = name
    '''
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
    Detail(1, "штуцер", 1),
    Detail(2, "Винт", 2),
    Detail(3, "Втулка", 4),
    Detail(4, "Шпонка", 3),
    Detail(5, "Пружина", 4),
    Detail(6, "Шпонка2", 5)
]
'''
#
 
emps_deps = [
    EmpDep(1,1),
    EmpDep(2,2),
    EmpDep(3,3),
    EmpDep(3,4),
    EmpDep(3,5),
 
    EmpDep(11,1),
    EmpDep(22,2),
    EmpDep(33,3),
    EmpDep(33,4),
    EmpDep(33,5),
]
'''
 
def main():
    """Основная функция"""
 
    # Соединение данных один-ко-многим 
    one_to_many = [(d.name, m.name) 
        for m in man 
        for d in det 
        if d.man_id == m.id]
    
    # Соединение данных многие-ко-многим
    '''
    many_to_many_temp = [(d.name, ed.dep_id, ed.emp_id) 
        for d in deps 
        for ed in emps_deps 
        if d.id==ed.dep_id]
    
    many_to_many = [(e.fio, e.sal, dep_name) 
        for dep_name, dep_id, emp_id in many_to_many_temp
        for e in emps if e.id==emp_id]
        '''
 
    print('Задание А1')
    res_1 = {}
    for i in one_to_many:
        if i[1][0] == 'А':
            if res_1.get(i[1]) == None:
                res_1[i[1]] = [i[0]]
            else: 
                res_1[i[1]].append(i[0])
    print(res_1)
    '''
    print('\nЗадание А2')
    res_12_unsorted = []
    # Перебираем все отделы
    for d in deps:
        # Список сотрудников отдела
        d_emps = list(filter(lambda i: i[2]==d.name, one_to_many))
        # Если отдел не пустой        
        if len(d_emps) > 0:
            # Зарплаты сотрудников отдела
            d_sals = [sal for _,sal,_ in d_emps]
            # Суммарная зарплата сотрудников отдела
            d_sals_sum = sum(d_sals)
            res_12_unsorted.append((d.name, d_sals_sum))
 
    # Сортировка по суммарной зарплате
    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)
 
    print('\nЗадание А3')
    res_13 = {}
    # Перебираем все отделы
    for d in deps:
        if 'отдел' in d.name:
            # Список сотрудников отдела
            d_emps = list(filter(lambda i: i[2]==d.name, many_to_many))
            # Только ФИО сотрудников
            d_emps_names = [x for x,_,_ in d_emps]
            # Добавляем результат в словарь
            # ключ - отдел, значение - список фамилий
            res_13[d.name] = d_emps_names
 
    print(res_13)
    '''
 
if __name__ == '__main__':
    main()
