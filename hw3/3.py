import os

def lines_generator(filename):
    f = open(filename, "r")
    while True:
        for line in f:
            yield line.strip()
        f.seek(0)


generator = lines_generator("file_0.txt")
for i, line in enumerate(generator):
    print(line)
    if i > 15:
        break
