def findKey(array, key):

  for i in range(len(array)):
    if array[i] == key:
      return i
      
  return -1

array = [1, 2, 5, 4, 0]
key = 4
print('key is at index : ',findKey(array, key))

array = [11, 22, 33, 44]
key = 33
print('key is at index : ',findKey(array, key))
