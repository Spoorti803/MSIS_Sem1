"""
Find the sum of last ‘n’ nodes in single linked list. Where ‘n’ will be given. Sum should be 
calculated with one iteration.
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
  
    def AddElement(self,data):
        new_node = Node(data)
        nodes =0
        if self.head is None:
            self.head = new_node
            nodes +=1
            return
        current = self.head
        while current.next:
            nodes+=1
            current = current.next
        current.next = new_node
        print(nodes)

    def display(self):
        if self.head is None:
            print("Linked list is empty")
            return
        current = self.head
        while current:
            print(current.data,end =" ")
            current = current.next
        print()


sll = SLL()
sll.AddElement(10)
sll.AddElement(20)
sll.AddElement(30)
sll.AddElement(40)
sll.AddElement(50)
sll.display()
