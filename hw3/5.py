import os

def lines_generator(filename):
    f = open(filename, "r")
    while True:
        for line in f:
            yield line.strip()
        f.seek(0)

generator = lines_generator("file_0.txt")

contains_nod = filter(lambda line: "NOD19" in line, generator)

for i, lines in enumerate(contains_nod):
    print(lines)
    if i > 15:
        break
