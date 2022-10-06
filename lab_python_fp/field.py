# Пример:
# goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

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
            print(s)
        else :
            print(result)
    
    

goods = [{'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}]
field(goods, 'title') 
field(goods, 'price', 'title') 
