def lru_cache(function):
    cache = {}

    def wrapper(*args, **kwargs):
        key = list(args)
        key.append(tuple(zip(kwargs.keys(), kwargs.values())))
        key = tuple(key)
        if key in cache.keys():
            return cache[key]
        value = function(*args, **kwargs)
        cache[key] = value
        return value

    return wrapper

@lru_cache
def some_function(*args, **kwargs):
    print(args)
    print(kwargs)

some_function(5, 4, k=2)

some_function(5, 4, k=2)

some_function(1, k=5, l=7)

some_function(5, 4, k=2)
