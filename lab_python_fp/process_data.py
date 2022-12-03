import json
import sys
from gen_random import gen_random
from unique import Unique
from print_result import print_result
import cm_timer
from field import field

path = '/home/dasha/Desktop/BIKT/BIKT/lab_python_fp/data_light.json'

with open(path) as f:
    data = json.load(f)

@print_result
def f1(arg):
    return list(Unique([x['job-name'] for x in arg]))


@print_result
def f2(arg):
    return list(filter(lambda s: s.startswith('Программист'), arg))

@print_result
def f3(arg):
    return list(map(lambda s: s + ' с опытом Python', arg))


@print_result
def f4(arg):
    return list(zip(arg, gen_random(len(arg), 100000, 200000)))


if __name__ == '__main__':
    with cm_timer.cm_timer_1():
        f4(f3(f2(f1(data))))