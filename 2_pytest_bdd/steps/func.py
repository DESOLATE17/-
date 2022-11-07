def my_sort1(data):
    return sorted(data, key = abs, reverse = True)

def my_sort2(data):
    return sorted(data, key = lambda n: -abs(n))

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


