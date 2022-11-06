import random

def gen_random(num_count, begin, end):
    for i in range (0, num_count, 1):
        yield (random.randint(begin, end)) 

#gen_random(5, 1, 3)