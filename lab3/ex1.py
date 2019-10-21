#1
iter_list = ["12", "-2", "0"]

result = list(map(int, iter_list))

print(result)

#2
words_list = ["hello", "world"]

result = list(map(len, words_list))

print(result)

#3
result = list(map(lambda word: word[::-1], words_list))

print(result)

#4
range_list = [x for x in range(2, 6)]

result = list(map(lambda x: tuple([x ** i for i in range(1, 4)]), range_list))

print(result)

#5

result = list(map(lambda a: list(a)[0] * list(a)[1], zip(range(2, 6), range(3, 9, 2))))

print(result)
