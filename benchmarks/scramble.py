import timeit

import random

def scramble_1(lst):
    """
    Scrambles a list.

    Taken from eumiro at https://stackoverflow.com/a/9770686.
    """
    dest = lst[:]
    random.shuffle(dest)
    return dest


def scramble_2(lst):
    """
    Scrambles a list.

    Taken from koffein at https://stackoverflow.com/a/19836008.
    """
    return sorted(lst, key = lambda _: random.random())


if __name__ == "__main__":
    lst = [random.random() for _ in range(int(1e3))]
    
    number = 1e4

    print(timeit.timeit("scramble_1(lst)", globals=locals(), number=int(number)))

    print(timeit.timeit("scramble_2(lst)", globals=locals(), number=int(number)))

    