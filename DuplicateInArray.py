def duplicates(array):
  visited = set()
  duplicates = []

  for element in array:
    if element in visited:
      duplicates.append(element)
    else:
      visited.add(element)

  return duplicates

array = [1, 2, 4, 5, 2, 1]
print(duplicates(array))
