"""
Assume that we have two linked lists. Elements in individual list are unique.
There may be identical elements across linked lists. 
Create a third list which contains only common elements across first two lists.
"""
class Node:
  def __init__(self,data):
    self.data = data
    self.next =None

class SinglyLinkedList:
  def __init__(self):
    self.head = None

  #adding elements at the end
  def AddElement(self,data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return
    current = self.head
    while current.next:
      current = current.next
    current.next = new_node

  def display(self):
    if self.head is None:
      print("Linked list is empty")
    current = self.head
    while current:
      print(current.data,end=" ")
      current = current.next
    print()


print("Add elements to linked list 1")
sll1 = SinglyLinkedList()
sll1.AddElement(10)
sll1.AddElement(20)
sll1.AddElement(30)
sll1.AddElement(50)
print("Linked List 1 contains: ")
sll1.display()
print()
print("Add elements to linked list 2")
sll2 = SinglyLinkedList()
sll2.AddElement(20)
sll2.AddElement(30)
sll2.AddElement(40)
sll2.AddElement(50)
print("Linked List 2 contains: ")
sll2.display()
print()

print("Add Common elemnts from 1 and 2 to Linked list 3: ")
def CreateLinkedList3(sll1,sll2):
  sll3 = SinglyLinkedList()
  current1 = sll1.head
  while current1:
    current2 = sll2.head
    while current2:
      if current1.data == current2.data:
        sll3.AddElement(current1.data)
      current2 = current2.next
    current1 = current1.next
  return sll3

sll3 = CreateLinkedList3(sll1,sll2)
print()
print("Linked List 3 contains: ")
sll3.display()