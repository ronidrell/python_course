import itertools
import operator
from functools import reduce

def dot_product(u, v):
    return reduce(lambda x, y: x + y,
                  itertools.starmap(operator.mul, itertools.zip_longest(u, v, fillvalue=1)))

print(dot_product([1, 3, 5], [2, 4, 6]))

