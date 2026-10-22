def BinarySearch(arr,key):
    n = len(arr)
    low =0
    high = n-1
    while low<=high:
        mid = (low+high)//2
        if key == arr[mid]:
            return mid
        elif key <arr[mid]:
            high = mid-1
        else:
            low = mid+1

    return -1


arr = list(map(int,input("Enter the array neede ").split()))
key = int(input("Enter the element to be found: "))
if arr == sorted(arr):
    val = BinarySearch(arr,key)
    if val !=-1:
        print("The given elment is found at the position: ",val)
    else:
        print("The required element is not found")
else:
    print("The array must be sorted")