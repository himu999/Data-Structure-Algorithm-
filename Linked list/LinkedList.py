class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data=None):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        for data in data_list:
            self.insert_at_end(data)

    def length_of_ll(self):
        itr = self.head
        cont = 0

        while itr:
            cont += 1
            itr = itr.next

        return print(cont)


    def print(self):

        if self.head is None:
            print("Empty Linked List")
            return

        itr = self.head
        llsr = ""

        while itr:
            llsr += str(itr.data)+"-->"
            itr = itr.next

        print(llsr)


if __name__ == "__main__":

    llst = LinkedList()
    dat_list = ["mango", "banana", "guava"]
    llst.insert_values(dat_list)
    llst.insert_at_beginning(10)
    llst.insert_at_beginning(15)
    llst.insert_at_end(5)
    llst.insert_at_end(15)
    llst.insert_at_end(25)
    llst.insert_at_end(35)
    llst.insert_at_end(45)
    llst.insert_at_end(55)
    llst.insert_at_end(65)
    llst.insert_at_end(75)
    llst.insert_at_end(85)
    llst.print()
    llst.length_of_ll()

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_the_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_the_end(self, data=None):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_value(self, data_list):
        # self.head = None
        for data in data_list:
            self.insert_at_the_end(data)

    def length_linked_list(self):
        itr = self.head
        cont = 0

        while itr:
            itr = itr.next
            cont += 1

        print(cont)

    def remove_element(self, index):
        if index > 0 or index>= self.length_linked_list():
            raise Exception("Invalid index")

    def print(self):

        if self.head is None:
            print("Linked List is empty")
            return

        itr = self.head
        strng = ""

        while itr:
            strng += str(itr.data)+"-->"
            itr = itr.next

        print(strng)


if __name__ == "__main__":
    ll = LinkedList()

    ll.insert_at_the_end(10)
    ll.insert_at_the_end(20)
    ll.insert_at_the_end(30)
    ll.insert_at_the_end(100009897554540)
    ll.insert_at_the_end(40)
    ll.insert_at_the_end(50)
    ll.insert_at_the_end(60)
    ll.insert_at_the_end(70)
    ll.insert_at_the_end(80)
    ll.insert_at_the_end(90)
    ll.insert_at_the_end(100)
    ll.insert_at_the_end(101)
    ll.insert_at_the_beginning(9)
    ll.insert_at_the_beginning(99)
    ll.insert_at_the_beginning(69)
    ll.insert_at_the_beginning(96)
    ll.insert_at_the_beginning(90)
    ll.insert_at_the_beginning("09")
    lst = ["hey", "you", "sdd"]
    ll.insert_value(lst)
    ll.print()
    ll.length_linked_list()
