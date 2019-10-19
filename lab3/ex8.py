from itertools import zip_longest

matrix = (
    (1, 2, 3, 4),
    (5, 6, 7, 8),
    (9,10,11,12)
)

def transpose(m):
    return tuple(zip(*m))

print(matrix)

print(transpose(matrix))