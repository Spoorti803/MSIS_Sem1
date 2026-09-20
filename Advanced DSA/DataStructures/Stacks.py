class Stack:
    def __init__(self,capacity):
        self.stack = []
        self.capacity = capacity 
        self.top = -1

    def isEmpty(self):
        return self.top==-1
           

    def isFull(self):
        return self.top==self.capacity-1
            

    def Push(self,data):
        if self.isFull():
            print("Stack is full")
            return
        self.top +=1
        self.stack.append(data)

    def Pop(self):
        if self.isEmpty():
            print("Stack is empty")
            return None
        data = self.stack[self.top]
        self.stack.pop()
        self.top -=1
        return data

    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
            return None
        return self.stack[self.top]

    def stackTraversal(self):
        if self.isEmpty():
            print("Stack is empty")
            return
        for i in range(self.top,-1,-1):
            print(f"{i}: {self.stack[i]}")

def getInput(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a number")

def main():
    stack = Stack(getInput("Enter the size of stack: "))
    while True:
        print("Stack Implementation")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")

        choice = getInput("Enter your choice: ")

        if choice==1:
            data = getInput("Enter the data: ")
            stack.Push(data)
        elif choice==2:
            data = stack.Pop()
            if data is not None:
                print("The deleted element is: ",data)
        elif choice ==3:
            data = stack.peek()
            if data is not None:
                print("Top element: ",data)
        elif choice==4:
            stack.stackTraversal()
        elif choice==5:
            print("Exiting...")
            break
        else:
            print("Invalid entry...please try again")


if __name__=="__main__":
    main()

