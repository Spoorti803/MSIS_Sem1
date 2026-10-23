def heapify(arr,n,i):
    larges =i
    left = 2*i+1
    right = 2+i*2

    if left<n and arr[left] >arr[larges]:
        larges = left
    if right<n and arr[right]>arr[larges]:
        larges=right

    if larges!=i:
        arr[i],arr[larges] = arr[larges],arr[i]
        heapify(arr,n,larges)

def heapsort(arr):
    n = len(arr)

    #build max heap
    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)

    #sort
    for i in range(n-1,0,-1):
        arr[0],arr[i] = arr[i],arr[0]
        heapify(arr,i,0)

    return arr

arr =[40,10,30,50,20]
print("Original array: ",arr)
heapsort(arr)
print("Sorted: " ,arr)