class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def lenList(self):
        count = 0
        temp = self.head
        # while True:
        #     count+=1
        #     if temp.next is None:
        #         break
        #     temp = temp.next
        # same as:
        while temp is not None:
            count+=1
            temp = temp.next
        print(f'count is {count}')
        return count
        
            
        
    def insertEnd(self, newVal):
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
            
        print(self.head.val)
        print(self.head.next)
        print(" ")
        
    def printList(self):
        currValue = self.head
        if self.head is None:
            print("List is empty")
        else:
            while True:
                print(currValue.val)
                currValue = currValue.next
                if currValue is None:
                    break
                                
    def insertFirst(self, firstVal):
         temp = self.head
         self.head = firstVal
         self.head.next = temp
         del temp
        # if self.head is None:
        #     self.head = firstVal
        # else:
        #     temp = self.head
        #     self.head = firstVal
        #     self.head.next = temp
        #     del temp
        
    def insertMid(self, midVal, pos):
        if pos < 0 or pos > self.lenList():
            print("Invalid position entered")
            return 
        
        if pos == 0:
            self.insertFirst(midVal)
            return
       
        count = 0
        currNode = self.head
        while True:
            if count == pos:
                prevNode.next = midVal
                midVal.next = currNode
                break
            prevNode = currNode
            currNode = currNode.next
            count+=1
            
        
        # while count < pos:
        #     prevNode = currNode
        #     currNode = currNode.next
        #     count+=1
        # prevNode.next = midVal
        # midVal.next = currNode
        
        
        
        # print(newNode.next.val)
    def deleteit(self):
        temp=self.head
        self.head = self.head.next
        del(temp)
        
        
    def delFirst(self):
        if self.head is not None:
            self.deleteit()
    
    def delPos(self, pos):
        if pos < 0 or pos > self.lenList():
            print("Invalid position")
        count = 0
        curr = self.head
        while True:
            if count == pos:
                prev.next = curr.next
                curr.next = None
                break
            prev = curr
            curr = curr.next
            count += 1
            
     
    def delLast(self):
        currNode = self.head
        while currNode.next is not None:
            prevNode = currNode
            currNode = currNode.next
        prevNode.next = None
               
    def delAll(self):
        while self.head is not None:
            self.deleteit()
        
        
    
    
        
                
                
            
firstNode = Node(1)
linkedlist = LinkedList()
linkedlist.insertEnd(firstNode)
secondNode = Node(2)
linkedlist.insertEnd(secondNode)
thirdNode = Node(3)
linkedlist.insertEnd(thirdNode)
fourthNode = Node(4) 
linkedlist.insertFirst(fourthNode)
print("Begin printing")
linkedlist.printList()

linkedlist.lenList()

print("Begin printing insert list")
fifthNode = Node(5)
linkedlist.insertMid(fifthNode,4)
linkedlist.printList()
print("Stop printing insert list")
print("del at printing")
linkedlist.delPos(5)
linkedlist.printList()
print("del at printing")

linkedlist.delFirst()
linkedlist.printList()
print("print del last")
linkedlist.delLast()
linkedlist.printList()
print("Begin printing del")
print("Begin printing delAll")
linkedlist.delAll()
linkedlist.printList()

# print(linkedlist)
# print(firstNode)