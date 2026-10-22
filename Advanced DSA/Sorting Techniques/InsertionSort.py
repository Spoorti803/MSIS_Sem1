def InsertionSort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1

        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j=j-1
        arr[j+1] = key

    return arr

#user input
arr = list(map(int,input("Enter the unsorted array: ").split()))
print("Insertion sort: ",InsertionSort(arr))
