class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def AddAtFirst(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def AddAtGivenPosition(self,data,loc):
        new_node = Node(data)
        count =1
        current = self.head
        while current.next!=None and count<loc-1:
            current = current.next
            count +=1
        new_node.next = current.next
        current.next = new_node
        

        


    def AddAtLast(self,data):
        new_node = Node(data)
        if self.head==None:
            self.head = new_node

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def DeleteAtStart(self):
        if self.head == None:
            print("The list is empty")
        print("Element deleted is: ",self.head.data)
        self.head = self.head.next

    def DeleteAtLast(self):
        if self.head == None:
            print("The linked list is empty")
        current = self.head
        while current.next.next!=None:
            current=current.next
        print("element to be deleted is: ",current.next.data)
        current.next= None

    def display(self):
        if self.head == None:
            print("The linked list is empty")
        current = self.head
        print("Linked List: ")
        while current:
            print(current.data ,end=" ")
            current = current.next
        print()


sll = SinglyLinkedList()
sll.AddAtFirst(21)
sll.AddAtFirst(31)
sll.AddAtLast(100)
sll.AddAtFirst(200)
sll.AddAtLast(400)
sll.AddAtLast(1000)
sll.AddAtFirst(999)
sll.display()
sll.DeleteAtStart()
sll.DeleteAtLast()
sll.display()
sll.AddAtGivenPosition(99,3)
sll.display()