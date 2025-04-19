from search import Trie

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
    def remove_by_key_value(self,key,value):
        current = self.head
        previous_node = None
        while current:
            if key in current.val and current.val[key] == value:
                if previous_node:
                    previous_node.next = current.next
                else:
                    self.head = current.next
                return 
            previous_node = current
            current = current.next
        print('No Match found.')
linked_list = LinkedList()
trie = Trie()
def add_contact():
    name = input('Enter name: ')
    number = input('Enter number: ')
    name = Node({name: number})
    linked_list.add_to_tail(name)
    trie.add(name)
    trie.add(number)

on = True
while on:
    linked_list.display()
    user_input = int(input('To add a contact press (1).' \
    'To remove a contact press (2).' \
    'To search a contact press (3): '))
    match user_input:
        case 1:
            add_contact()
        case 2:
            name_remove = input('Please enter the name you would like to remove: ')
            number_to_remove = input('Please enter the number of contact you would like to delete: ')
            use_check = input(f'Please type (Y)es that you would like to remove {name_remove}:{number_to_remove} ').upper()
            if use_check == 'Y' or use_check == 'YES':
                linked_list.remove_by_key_value(name_remove,number_to_remove)
        case 3:
            pass
