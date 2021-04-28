from node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append_node(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = node
            return
        else:
            self.tail.next = node
            self.tail = self.tail.next

    # adds a new Node to the beginning of the list and sets the pointer to the former head node.
    def prepend_node(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # contain method returns a message and the matching data returns None if there is no match.
    # https://www.youtube.com/watch?v=Ast5sKQXxEU
    def does_contain(self, number):
        current_node = self.head
        while current_node:
            if current_node.data == number:
                print('ITS A MATCH')
                return number
            else:
                current_node = current_node.next
        return None

    # Binary Tree
    
