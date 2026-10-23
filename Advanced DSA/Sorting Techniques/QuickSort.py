def quick_Sort(arr,low,high):
    if low <high:
        pivot_index = partition(arr,low,high)

        quick_Sort(arr,low,pivot_index-1)
        quick_Sort(arr,pivot_index+1,high)

    return arr


def partition(arr,low,high):
    pivot = arr[high]
    i = low -1
    for j in range(low,high):
        if arr[j]<=pivot:
            i=i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1


arr = [5,3,8,1,2]
n = len(arr)-1
print(quick_Sort(arr,0,n))