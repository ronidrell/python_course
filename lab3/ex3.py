from functools import reduce
from math import gcd

# gdc наибольший общий делитель
# наименьшее общее кратное

def lcm(*nums):
    if nums != ():
        return reduce(lambda x, y: (x * y) // gcd(x, y), nums)
    return 1

print(lcm(3, 5))
print(lcm(41, 106, 12))
print(lcm(1, 2, 6, 24, 120, 720))
print(lcm(3))
print(lcm())