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
