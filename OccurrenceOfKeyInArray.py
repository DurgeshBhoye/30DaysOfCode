def keyOccurr(array, key):
  count = 0

  for element in array:
    if element == key:
      count += 1

  return count

array = [1, 2, 3, 1, 5, 1, 8]
key = 1
print(keyOccurr(array, key))
