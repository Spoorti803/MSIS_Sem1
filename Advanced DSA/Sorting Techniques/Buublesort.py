#Bubble sort
def Bubblesort(arr):
  n = len(arr)
  for i in range(n):
    for j in range(n-i-1):
      if arr[j+1] <arr[j]:
        arr[j],arr[j+1] = arr[j+1],arr[j]

  return arr


arr = list(map(int,input("Enter the required unsorted array: ").split()))
print("The sorted array is: ",Bubblesort(arr))