class Node(object):
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList(object):
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        if self.head == None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node

    def print(self):
        if self.head is None:
            print("Linked List is empty")

        itr = self.head
        s = ""
        while itr:
            s += str(itr.data) + "-->"
            itr = itr.next
        print(s)


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_at_beginning(10)
    dll.insert_at_beginning(20)
    dll.insert_at_beginning(30)
    dll.print()
