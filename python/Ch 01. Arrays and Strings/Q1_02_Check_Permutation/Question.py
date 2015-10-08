# Using a python dict to count the number of each char
# O(n) where n is the length of the longest string
def is_permutation_dict(str1, str2):
  """
  >>> is_permutation_dict("aaabbb", "ababba")
  True
  >>> is_permutation_dict("abccd", "abcab")
  False
  """
  if len(str1) != len(str2):
    return False
  alphabet1 = {}
  alphabet2 = {}
  for letter in str1:
    if letter in alphabet1:
      alphabet1[letter] += 1
    else:
      alphabet1[letter] = 0 
  for letter in str2:
    if letter in alphabet2:
      alphabet2[letter] += 1
    else:
      alphabet2[letter] = 0
  return alphabet1.items() == alphabet2.items()

# Using string sort
# O(logn) where n is the length of the longest string
def is_permutation_sort(str1, str2):
  """
  >>> is_permutation_sort("aaabbb", "ababba")
  True
  >>> is_permutation_sort("abccd", "abcab")
  False
  """
  return sorted(str1) == sorted(str2)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
