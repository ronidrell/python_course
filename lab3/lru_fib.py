import time

def lru(function):
    cache = {}

    def wrapper(*args):
        if args in cache.keys():
            return cache[args]
        value = function(*args)
        cache[args] = value
        return value

    return wrapper

@lru
def fib_lru(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fib_lru(n - 1) + fib_lru(n - 2)

t0 = time.time()
print(fib(15))

print(time.time() - t0)

t0 = time.time()
print(fib_lru(15))

print(time.time() - t0)