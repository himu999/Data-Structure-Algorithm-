class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self,  data):
        if self.head is None:
            self.head = Node(data, None)
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        for data in data_list:
            self.insert_at_end(data)

    def insert_at(self, index, data):
        if index < 0 or index >= self.length():
            raise Exception('Error!')

        if self.head is None:
            self.insert_at_beginning(data)
            return

        itr = self.head
        count = 1
        while itr:
            if index-1 == count:
                itr.next = Node(data, itr.next)
                break
            itr = itr.next
            count += 1

    def removes_at(self, index):
        if index < 0 or index >= self.length():
            raise Exception('Error!')
        if index == 0:
            print("Linked List is empty")
            return

        itr = self.head
        count = 1
        while itr:
            if index-1 == count:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def removes_by_value(self, val):
        if self.head is None:
            return print('Linked List is empty')
        if self.head.data == val:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == val:
                itr.next = itr.next.next
                break
            itr = itr.next

    def length(self):
        if self.head is None:
            print('Linked List is empty!')
            return
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count

    def print(self):
        if self.head is None:
            print('Linked List is empty')

        itr = self.head
        lls = ''

        while itr:
            lls += str(itr.data) + '-- > '
            itr = itr.next
        print(lls)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(1)
    ll.insert_at_beginning(2)
    ll.insert_at_beginning(3)
    ll.insert_at_beginning(4)
    ll.insert_at_beginning(5)
    ll.insert_at_end(6)
    ll.insert_at_end(7)
    ll.insert_at_end(8)
    ll.insert_values(["lily", 'was', 'little', 'girl'])
    ll.print()
    ll.length()
    ll.insert_at(4, 10)
    ll.print()
    ll.removes_at(4)
    ll.print()
    ll.removes_by_value(8)
    ll.print()
