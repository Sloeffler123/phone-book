

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

    def set_next(self,node):
        self.next = node   
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    # this allows us to use a for loop over objects
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
    # This uses iter to loop through all nodes and finds the last then tells the last one to set its next pointer to the node we pass in
    def add_to_tail(self,node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.tail.set_next(node)
        self.tail = node

    def add_to_head(self,node):
        if self.head is None:
            self.tail = node
        node.set_next(self.head)
        self.head = node
    def display(self):
        current = self.head
        while current:
            print(current.val, end=' -> ')
            current = current.next
        print('None')    
        