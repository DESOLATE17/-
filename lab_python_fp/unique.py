# Итератор для удаления дубликатов
import gen_random

class Unique(object):
    def __init__(self, items, **kwargs):
        self.seen = []
        for i in items: #AbC
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
            return StopIteration
        item = self.seen[0]
        del self.seen[0]
        return item

    def __iter__(self):
        return self


print("1st test")

data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']

t = Unique(data, ignore_case = True)

print(next(t))
print(next(t))

#print(next(t))


print("2nd test")

data = [1,1,1,1,1,1,2,2,2,2,2,2]

t = Unique(data)

print(next(t))
print(next(t))


print("3rd test")
data = gen_random.gen_random(10, 1, 3)

t = Unique(data)

print(next(t))
print(next(t))
print(next(t))
