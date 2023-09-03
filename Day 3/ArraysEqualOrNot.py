def areEqual(array_a, array_b):

  if len(array_a) != len(array_b):
    return False

  for i in range(len(array_a)):
    if array_a[i] != array_b[i]:
      return False

  return True

array_a = [1, 2, 5, 4, 0]
array_b = [1, 2, 5, 4, 0]

print(areEqual(array_a, array_b))

array_a = [1, 2, 3, 4, 5]
array_b = [11, 22, 33, 44]

print(areEqual(array_a, array_b))
