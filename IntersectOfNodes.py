class LinkedList:
    # node class
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None
        
    def __init__(self):
     # head of node    
     self.headA = None
     self.headB = None
     # add value to node
    def addA(self, data):
         node = self.Node(data)
         if self.headA == None:
             self.headA = node
         else:
             current = self.headA
             while current.next:
                 current = current.next
             current.next = node
             
    def addB(self, data):
         node = self.Node(data)
         if self.headB == None:
             self.headB = node
         else:
             current = self.headB
             while current.next:
                 current = current.next
             current.next = node
    
# QUESTION ASWER
    def intersectNode(self, val):
        temp = self.headA
        while temp.next is not None:
        	temp = temp.next
        hold = self.headB
        while hold.value != val:
        	hold = hold.next
        temp.next = hold        

    def getIntersectionNode(self, headA, headB):
        while headA is not None:
            temp = headB
            while temp is not None:
                if headA is temp:
                    return headA
                temp = temp.next
            headA = headA.next
        return None

    # Display Answer
    def displayAns(self):
        result = self.getIntersectionNode(self.headA, self.headB)
        print(result.value if result else None)
	
# lets try it
list = LinkedList()
list.addA(4)
list.addA(1)

list.addB(5)
list.addB(6)
list.addB(1)
list.addB(8)
list.addB(4)
list.addB(5)
list.intersectNode(8)
list.displayAns()

