def field(items, *args):
    result = {}
    assert len(args) > 0
    for d in items:
        for i,j in d.items():
            if i in args:
                result[i] = j
        if len(result) == 1:
            s = result.popitem()
            s = "'" + str(s[1]) + "'" 
            yield s 
        else :
            yield result     
    
if __name__ == '__main__':
    goods = [{'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}]
    for i in field(goods, 'title'):
        print(i)
    for i in field(goods, 'price', 'title'):
        print(i)
            