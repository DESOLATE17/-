def print_result(func):
    def inner(*args, **kwargs):
        print(func.__name__)
        res = func(*args, **kwargs)
        if type(res) == list:
            for i in res:
                print(i)
        elif type(res) == dict:
            for key in res.keys():
                print(f'''{key} = {res[key]}''')
        else:
            print(res)
    return inner

@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()