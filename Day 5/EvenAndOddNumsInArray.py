def find_even_odd_numbers(array):
  """Finds the even and odd numbers in array."""
  even_numbers = []
  odd_numbers = []
  for number in array:
    if number % 2 == 0:
      even_numbers.append(number)
    else:
      odd_numbers.append(number)
  return even_numbers, odd_numbers


array1 = [1, 2, 5, 4, 0]
even_numbers_case_1, odd_numbers_case_1 = find_even_odd_numbers(array1)

array2 = [11, 22, 33, 44]
even_numbers_case_2, odd_numbers_case_2 = find_even_odd_numbers(array2)

print("Even numbers:",even_numbers_case_1)
print("Odd numbers:", odd_numbers_case_1, "\n")

print("Even numbers:", even_numbers_case_2)
print("Odd numbers:", odd_numbers_case_2)
