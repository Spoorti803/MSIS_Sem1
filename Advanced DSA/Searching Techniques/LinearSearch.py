def LinearSearch(arr,target):
    n = len(arr)
    for i in range(n):
        if arr[i] == target:
            return i

    return -1



arr = [3,4,5,6,7]
target = int(input("Enter the element to be searched: "))
found = LinearSearch(arr,target)
if found == -1:
    print("The given element is not found")
else:
    print("The given element is at the position: ",found)