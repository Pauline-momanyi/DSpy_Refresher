class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert(self, newVal):
        if self.head is None:
            self.head = newVal
        else:
    #         # self.head.next = newVal => this will always rewrite the self.head.next
    #         # instead traverse the whole list
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newVal
            
        print(self.head)
        print(self.head.next)
        
    def printList(self):
        currValue = self.head
        if self.head is None:
            print("List is empty")
        else:
            while True:
                if currValue is None:
                    break
                print(currValue.val)
                currValue = currValue.next
                                
                
                
            
firstNode = Node(1)
linkedlist = LinkedList()
linkedlist.insert(firstNode)
secondNode = Node(2)
linkedlist.insert(secondNode)
thirdNode = Node(3)
linkedlist.insert(thirdNode)
print("Begin printing")
linkedlist.printList()

# print(linkedlist)
# print(firstNode)