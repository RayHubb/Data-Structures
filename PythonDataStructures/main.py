from linkedlist import LinkedList


if __name__ == '__main__':
    linked_list = LinkedList()

    linked_list.append_node(55)
    linked_list.append_node(60)
    linked_list.append_node(65)
    linked_list.prepend_node(50)
    print(linked_list.does_contain(65))



