
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularSLL:
    def __init__(self):
        self.head = None

    def addElements(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        current = self.head
        while current.next != self.head:
            current = current.next

        current.next = new_node
        new_node.next = self.head

    def removeOddElements(self):
        if self.head is None:
            return

        # Remove odd-valued nodes from the head
        while self.head is not None and self.head.data % 2 != 0:
            if self.head.next == self.head:
                self.head = None
                return

            last = self.head
            while last.next != self.head:
                last = last.next

            self.head = self.head.next
            last.next = self.head

        if self.head is None:
            return

        # Remove odd-valued nodes after the head
        current = self.head

        while current.next != self.head:
            if current.next.data % 2 != 0:
                current.next = current.next.next
            else:
                current = current.next

    def display(self):
        if self.head is None:
            print("Linked list is empty")
            return

        current = self.head
        while True:
            print(current.data, end=" ")
            current = current.next
            if current == self.head:
                break
        print()


csll = CircularSLL()
csll.addElements(12)
csll.addElements(13)
csll.addElements(14)
csll.addElements(16)
csll.addElements(19)

print("Initial Linked List:")
csll.display()

csll.removeOddElements()

print("After removing odd elements:")
csll.display()
