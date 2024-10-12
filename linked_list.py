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
        # or use super : super().__init__(value) and pass the Node class - inheritance, but next is not initialized
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end = "->" )
            temp = temp.next
    
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node  
        else:
            self.tail.next = new_node 
            self.tail = new_node
        self.length += 1
        
    def pop(self):
        # usharemove so unare-assign tail na next
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        # print (temp)
        return temp.value
    
        
linked_list_1 = LinkedList(4)
print (linked_list_1.head.value)
print (linked_list_1.tail.value)
print (linked_list_1.length)
linked_list_1.append(2)
print (linked_list_1.print_list())
print (linked_list_1.length)

print(linked_list_1.pop())
print(linked_list_1.pop())
print(linked_list_1.pop())

