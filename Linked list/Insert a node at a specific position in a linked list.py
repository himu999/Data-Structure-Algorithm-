class Node:
    def __init__(self, dat=None, next=None):
        self.data = dat
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, dat):
        if self.head is None:
            self.head = Node(dat, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(dat, None)

    def insert_by_index(self, dat, inx):

        itr = self.head
        count = 0
        while itr:
            if count == inx-1:
                itr.next = Node(dat, itr.next)
                break
            itr = itr.next
            count += 1

    def print(self):
        if self.head is None:
            print('Linked List is none')
            return
        itr = self.head
        lls = ""
        while itr:
            if itr.next is not None:
                lls += str(itr.data) + "-->"
                itr = itr.next
            else:
                lls += str(itr.data)
                itr = itr.next
        print(lls)


if __name__ == "__main__":
    ll = LinkedList()
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    for j in range(n):
        ll.insert_at_end(a[j])
    data = int(input())
    index = int(input())
    ll.insert_by_index(data, index)
    ll.print()
