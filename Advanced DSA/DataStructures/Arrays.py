#implementing arrays = using list

class arrays:
    def __init__(self,array):
        self.array = array

    def isEmpty(self):
        return len(self.array) ==0

    def addElement(self,data):
        self.array.append(data)

    def addElementAtPosition(self,index,data):
        if index <0 or index > len(self.array):
            print("Invalid index")
            return
        self.array.insert(index,data)

    def deleteElementAtBeginning(self):
        try:
            return self.array.pop(0)
        except IndexError:
            print("the array is empty")

    def deleteElementFromGivenIndex(self,index):
        if index <0:
            print("Negative index values are not allowed")
            return
        try:
            return self.array.pop(index)
        except IndexError:
            print("The given index does not have any elemnt")

    def deleteElementFromLast(self):
        try:
            return self.array.pop()
        except IndexError:
            print("The array is empty")

    def arrayTraversal(self):
        if self.isEmpty():
            print("The array is empty")
            return 
        for i in range(len(self.array)):
            print(f"The value of element at {i} = {self.array[i]}")


def getInput(promt):
    while True:
        try:
            return int(input(promt))
        except ValueError:
            print("Please enter a valid number")
def main():
    values=[]
    arclass = arrays(values)

    while True:
        print("============   Menu  ===================")
        print("1. Add Element")
        print("2. Add Element at a given index")
        print("3. Delete an element from start")
        print("4. Delete an element from the given position")
        print("5. Delete element from the end")
        print("6. Display the array")
        print("7. Exit")

        choice = getInput("Enter your choice: ")

        if choice ==1:
            val = getInput("Enter the element to be added: ")
            arclass.addElement(val)
        elif choice ==2:
            data = getInput("Enter the data to be added: ")
            index = getInput("Enter the index at which this data should be added: ")
            arclass.addElementAtPosition(index,data)
        elif choice==3:
            data = arclass.deleteElementAtBeginning()
            if data is not None:
                print("The element deleted is: ",data)
        elif choice==4:
            index = getInput("Enter the index of element to be deleted: ")
            data = arclass.deleteElementFromGivenIndex(index)
            if data is not None:
                print("The deleted data is :" , data)
        elif choice ==5:
            data = arclass.deleteElementFromLast()
            if data is not None:
                print("The elment deleted is: ",data)
        elif choice==6:
            arclass.arrayTraversal()
        elif choice==7:
            print("Exiting...")
            break
        else:
            print("Invalid entry...Please try again")


if __name__ == "__main__":
    main()