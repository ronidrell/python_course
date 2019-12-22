class Fifo:
    def __init__(self, *args):
        self.elements = []
        for element in args:
            self.elements.append(element)
    def __repr__(self):
        return str(self.elements)
    def isEmpty(self):
        if not self.elements:
            return True
        else:
            return False
    def push(self, object):
        return self.elements.append(object)
    def pop(self):
        return self.elements.pop(0)


if __name__ == '__main__':
    example = Fifo(1, 2, 4, 7, 5)
    print(example)
    print(example.isEmpty())
    example.push(8)
    print(example)
    example.pop()
    example.pop()
    print(example)
    
