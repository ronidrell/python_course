import operator
from functools import reduce

def fact(n):
    if n == 0:
        return 1
    return reduce(operator.mul, range(1, n + 1))

print(fact(3))
print(fact(7))
