class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
# class LinkedList(Node):
#     def __init__(self, value) -> None:
#         super().__init__(value)
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1
        
# linked_list_1 = LinkedList(4)
# print (linked_list_1.value)

class LinkedList():
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self, value):
        new_node = Node(value)
        if self.head is not None:
            self.next.append(value)
            
        else:
            self.head = value
            self.tail = value
    
        
linked_list_1 = LinkedList(4)
print (linked_list_1.head.value)
print (linked_list_1.tail.value)
linked_list_1.append(2)
print (linked_list_1.print_list())

