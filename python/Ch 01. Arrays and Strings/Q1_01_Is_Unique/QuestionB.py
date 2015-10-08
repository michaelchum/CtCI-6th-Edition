# Brute force comparison
def is_unique_compare(input_str):
  """
  >>> is_unique_compare("abcd")
  True
  >>> is_unique_compare("abccd")
  False
  """
  for index, letter in enumerate(input_str):
    for sub_letter in input_str[index+1:]:
      if letter == sub_letter:
        return False
  return True

# Sort and compare
def is_unique_sort(input_str):
  """
  >>> is_unique_sort("abcd")
  True
  >>> is_unique_sort("abccd")
  False
  """
  input_str = sorted(input_str)
  for index, letter in enumerate(input_str):
    if index != len(input_str)-1 and letter == input_str[index+1]:
      return False
  return True

if __name__ == '__main__':
    import doctest
    doctest.testmod()
