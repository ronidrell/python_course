def lru_cache(function):
    cache = {}

    def wrapper(*args):
        if args in cache.keys():
            return cache[args]
        value = function(*args)
        cache[args] = value
        return value

    return wrapper

@lru_cache
def some_function(a, b):
    return a + b

print(some_function(1, 2))
