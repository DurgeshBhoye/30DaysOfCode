# sort in ascending order 
arr = [10, 2, 5, 3, 1]
arr.sort()
print(arr)



# sort in descending order 
def sortArrDesc(arr):
"""Sorts an array in descending order."""
  for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
      if arr[i] < arr[j]:
        arr[i], arr[j] = arr[j], arr[i]


arr = [10, 1, 5, 3, 2]
sortArrDesc(array)
print(array)
