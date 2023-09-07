
def firstOccur(arr, key):
  """Finds the first occurrence of key in array and returns its index."""
  for i in range(len(arr)):
    if arr[i] == key:
      return i
  return -1


arr1 = [0, 1, 2, 3, 4, 5]
key = 1

arr2 = [5, 4, 3, 2, 1, 0]

index1 = firstOccur(arr1, key)
index2 = firstOccur(arr2, key)

print(index1)
print(index2)
