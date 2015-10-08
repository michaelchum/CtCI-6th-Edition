# Using a python str replace
def replace_space(input_str, length):
  """
  >>> replace_space("Mr John Smith", 13)
  'Mr%20John%20Smith'
  """
  return input_str.replace(" ", "%20")

# Using char replacement

if __name__ == '__main__':
    import doctest
    doctest.testmod()
