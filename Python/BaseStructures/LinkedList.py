class Node:
    def __init__(self, data):
        self.item = data
        self.nref = None

class LinkedList:
    def __init__(self):
        self.start_node = None

     def insert_in_emptylist(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print("list is not empty")