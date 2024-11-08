def sort_dict_by_keys(dictionary):
  """Sorts a dictionary by its keys in ascending order.

  Args:
    dictionary: The dictionary to sort.

  Returns:
    A new dictionary with the same key-value pairs, sorted by keys.
  """

  sorted_keys = sorted(dictionary.keys())
  sorted_dict = {}
  for key in sorted_keys:
    sorted_dict[key] = dictionary[key]
  return sorted_dict

if __name__ == "__main__":
  user_input = input("Enter a dictionary (e.g., {'a': 1, 'c': 3, 'b': 2}): ")
  user_dict = eval(user_input)  # Safely evaluate the input string as a dictionary

  sorted_dict = sort_dict_by_keys(user_dict)
  print(sorted_dict)