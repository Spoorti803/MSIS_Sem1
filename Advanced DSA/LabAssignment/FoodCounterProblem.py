"""
There is only one food truck at present. THe queue of people increases and hence another food truck is added at the other side. 
Divide the queue of people in efficient way and dispaly the assigned number of people for each food truck
"""


class Node:
    def __init__(self, customer):
        self.customer = customer
        self.next = None

    def __repr__(self):
        return f"Node({self.customer})"


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, cust):
        new_node = Node(cust)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def dequeue(self):
        if self.head is None:
            raise IndexError("dequeue from empty queue")
        cust = self.head.customer
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.size -= 1
        return cust

    def split(self):
        """Splits this queue into two new Queue objects and returns them."""
        mid = self.size // 2
        first_half, second_half = Queue(), Queue()

        current = self.head
        for _ in range(mid):
            first_half.enqueue(current.customer)
            current = current.next

        while current:
            second_half.enqueue(current.customer)
            current = current.next

        return first_half, second_half

    def __str__(self):
        items = []
        current = self.head
        while current:
            items.append(str(current.customer))
            current = current.next
        return " ".join(items)


def get_valid_choice():
    while True:
        try:
            choice = int(input("Add people? Note: Only 0 or 1 is accepted: "))
            if choice in (0, 1):
                return choice
        except ValueError:
            pass
        print("Invalid input, try again.")


count = 0
q = Queue()
choice = 1

while choice:
    choice = get_valid_choice()
    if choice == 1:
        count += 1
        q.enqueue(count)

print("HEAD:", q.head)
if q.head is not None:
    print("HEAD CUSTOMER:", q.head.customer)

first, second = q.split()
print("First queue:", first)
print("Second queue:", second)