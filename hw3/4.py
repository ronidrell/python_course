import os

def lines_generator(filename):
    f = open(filename, "r")
    while True:
        for line in f:
            yield line.strip()
        f.seek(0)

generator = lines_generator("file_0.txt")

len_of_lines = map(len, generator)

for i, lens in enumerate(len_of_lines):
    print(lens)
    if i > 15:
        break
