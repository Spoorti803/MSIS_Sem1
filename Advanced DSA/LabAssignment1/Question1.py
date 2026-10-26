"""
Linked List assignments
1. Create Single Linked List class with following functionalities:
a. Add at head
b. Add at tail
c. Delete at head
d. Delete at tail
e. Add after given data
f. Delete after given data
g. Search an element
"""
class Node:
  def __init__(self,data):
    self.data = data
    self.next =None

class SinglyLinkedList:
  def __init__(self):
    self.head = None

  def Add_At_Head(self,data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
    print("Data ",new_node.data," is added")

  def Add_At_tail(self,data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return
    current = self.head
    while current.next:
      current = current.next
    current.next = new_node
    print("Data ",new_node.data," is added")

  def Delete_At_head(self):
    if self.head is None:
      return None
    print("data deleted: ",self.head.data)
    self.head = self.head.next

  def Delete_At_tail(self):
    if self.head is None:
      return None
    if self.head.next is None:
      print("Data ",self.head.data," is deleted")
      self.head = None
      return
    current = self.head
    while current.next.next != None:
      current = current.next
    print("Data ",current.next.data," is deleted")
    current.next = None

  def Add_After_Given_Data(self,data,new_data):
    new_node = Node(new_data)
    if self.head is None:
      print("The given data is not present ")
      return
    
    current = self.head
    while current and current.data != data:
      current = current.next
      
    if current is None:
      print("The given data is not present ")
      return
    new_node.next = current.next
    current.next = new_node
    print("Data ",new_node.data," is added")
      
  def Delete_After_Given_Data(self,data):
    if self.head is None:
      print("The Linked list is empty")
      return
    current = self.head
    while current and current.data != data:
      current = current.next
    
    if current is None:
      print("The given data is not present ")
      return
    if current.next is None:
      print("There is no data after the given data")
      return 
    print("Data ",current.next.data, " is deleted")
    current.next = current.next.next

  def Search_an_Element(self,key):
    if self.head is None:
      print("The Linked List is Empty")
      return
    position =1
    current = self.head
    while current:
      if current.data == key:
        print("The element ",current.data," is present at position ",position," in the linked list")
        return 
      position +=1
      current=current.next

  def display(self):
    if self.head is None:
      print("The linked list is empty ")
      return
    current = self.head
    while current:
      print(current.data,end=" ")
      current = current.next
    print()



sll = SinglyLinkedList()

print("-------Initail Linked list-------- ")

sll.display()
print()
print("--------Adding elements to the linked list--------")
sll.Add_At_Head(10)
sll.Add_At_Head(20)
sll.Add_At_Head(30)
sll.Add_At_tail(80)
sll.Add_After_Given_Data(20,40)
sll.Add_After_Given_Data(30,90)
print()
print("---------Linked list after adding elements---------")

sll.display()
print()
print("---------Deleting elements from the linked list---------")
sll.Delete_At_head()
sll.Delete_At_tail()
sll.Delete_After_Given_Data(30)
print()
print("---------Linked list after deleting elements-------")
sll.display()
print()
print("---------Searching an element in the linked list--------")
sll.Search_an_Element(20)
