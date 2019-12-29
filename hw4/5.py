class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        # self.last = None
        # self.length = 0

    def __str__(self):
        out = ""
        current = self.head
        if current.next is not None:
            current = current.next
        while current is not None:
            out += str(current.value) + '\n'
            current = current.next
        out += str(current)
        return out

    def clear(self):
        self.__init__()

    def add(self, x):
        new = Node(x)
        if self.head is None:
            self.head = new
            return
        tail = self.head
        while (tail.next):
            tail = tail.next
        tail.next = new



if __name__ == '__main__':
    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    print(ll)
