class LinkedList:
    class Node:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
    def __init__(self):
        self.head = None
     
    def add(self, val):
         node = self.Node(val)
         if self.head == None:
            self.head = node
            return
         temp = self.head
         while temp.next != None:
             temp = temp.next
         temp.next = node
    def display(self):
          temp = self.head
          while temp != None:
               print(f'{temp.val} -> ', end="")
               temp = temp.next
    # remove duplicate
    def removeDup(self):
        current = self.head
        while current != None:
            if current.next is not None and current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

link = LinkedList()
link.add(2)       
link.add(2) 
link.add(2)
link.add(3)
link.add(5)
link.add(5)
link.add(7)
link.add(9)
link.add(10)
link.display()
link.removeDup()
print()
print("Remove Duplicates: ")
link.display()