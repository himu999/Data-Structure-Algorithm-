class Node:
    def __init__(self, data=None, nxt=None):
        self.data = data
        self.nxt = nxt


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.nxt:
            itr = itr.nxt

        itr.nxt = Node(data, None)

    def insert_values(self, data_list):
        # self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.nxt)
                itr.nxt = node
                break

            itr = itr.nxt
            count += 1

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid index')

        if index == 0:
            self.head = self.head.nxt
            return

        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.nxt = itr.nxt.nxt
                break
            itr = itr.nxt
            count += 1

    def print(self):
        if self.head is None:
            print("Link list is empty")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + "-->"

            itr = itr.nxt
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head

        while itr:
            count += 1
            itr = itr.nxt
        return count


if __name__ == "__main__":
    ob = LinkedList()
    ob.insert_at_beginning(1)
    ob.insert_at_beginning(2)
    ob.insert_at_end(50)

    ob.insert_values(["name", "hi"])

    ob.print()
    ob.insert_at(4, "Himel")
    ob.remove_at(5)

    ob.print()
