def MergeSort(arr):
    n = len(arr)
    if n<=1:
        return arr
    mid = n//2
    left = MergeSort(arr[:mid])
    right = MergeSort(arr[mid:])
    res =[]
    i =0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1

    res.extend(left[i:])
    res.extend(right[j:])
    return res


#user input
arr = list(map(int,input("Enter the unsorted array: ").split()))
print("Merge Sort: ",MergeSort(arr))