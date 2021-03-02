class Node:

    def __int__(self, value):
        self.next = None
        self.prev = None
        self.value = value


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, val):
        node = Node(val)
        if self.tail is None:
            self.head = node
            self.tail = node
            self.size += 1
        else:
            self.head.next = node
            node.prev = self.head
            self.tail = node
            self.size += 1


my = DoubleLinkedList()

my.add(1)
my.add(5)
my.add(2)

print(my)


