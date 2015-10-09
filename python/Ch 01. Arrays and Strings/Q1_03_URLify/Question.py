# Using a python str replace
def replace_space(input_str, length):
  """
  >>> replace_space("Mr John Smith", 13)
  'Mr%20John%20Smith'
  """
  return input_str.replace(" ", "%20")

# Using char replacement
def replace_array(input_str, length):
  """
  >>> replace_space("Mr John Smith", 13)
  'Mr%20John%20Smith'
  """
  result = []
  for letter in input_str:
    if letter is not " ":
      result.append(letter)
    else:
      result.append('%20')
  return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
