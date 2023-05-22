# Singly Linked List

class  Node :
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList :
    def __init__(self):
        self.head = Node()

    def insertData(self, data):
        new_data = Node(data)
        cur = self.head
        while cur.next != None :
            cur = cur.next
        cur.next = new_data

    def display(self):
        disp = []
        cur = self.head
        while cur.next != None :
            cur =cur.next
            disp.append(cur.data)

        print(disp)


l = LinkedList()
l.insertData(1)
l.insertData(2)
l.insertData(3)
l.insertData(4)
l.insertData(5)
l.display()


