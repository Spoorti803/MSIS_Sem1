class Cque:
    def __init__(self,capacity):
        self.que = [None]*capacity
        self.capacity = capacity
        self.front =-1
        self.rear =-1

    def enqueue(self,data):
        if (self.rear+1)%self.capacity == self.front:
            print("overflow")
            return
        if self.front ==-1:
            self.front =0
        
        self.rear = (self.rear+1)%self.capacity
        self.que[self.rear] = data
        print(data," inserted")

    def dequeue(self):
        if self.front ==-1:
            print("underflow")
            return
        print("Deleted element is: ",self.que[self.front])

        if self.front==self.rear:
            self.rear = self.front=-1
        else:
            self.front=(self.front+1)%self.capacity

    def disply(self):
        if self.front==-1:
            print("underflow")
            return
        i=self.front
        while True:
            print(self.que[i],end=" ")
            if i ==self.rear:
                break
            i=(i+1)%self.capacity


qu = Cque(10)
qu.enqueue(2)
qu.enqueue(10)
qu.enqueue(100)
qu.enqueue(99)
qu.dequeue()
qu.disply()