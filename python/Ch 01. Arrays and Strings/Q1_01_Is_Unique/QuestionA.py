# Using the python set data structure
def is_unique_set(input_str):
  """
  >>> is_unique_set("abcd")
  True
  >>> is_unique_set("abccd")
  False
  """
  return len(set(input_str)) == len(input_str)

# Using the python dict data structure
def is_unique_dict(input_str):
  """
  >>> is_unique_dict("abcd")
  True
  >>> is_unique_dict("abccd")
  False
  """
  alphabet = {}
  for letter in input_str:
    if letter in alphabet:
      return False
    alphabet[letter] = True
  return True

# Using the python list data structure
def is_unique_list(input_str):
  """
  >>> is_unique_list("abcd")
  True
  >>> is_unique_list("abccd")
  False
  """
  alphabet_list = [False] * 256
  for letter in input_str:
    if alphabet_list[ord(letter)]:
      return False
    alphabet_list[ord(letter)] = True
  return True

if __name__ == '__main__':
    import doctest
    doctest.testmod()
