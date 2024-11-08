def is_palindrome(string):
    """Checks if a given string is a palindrome.

    Args:
        string: The input string to check.
    Returns:
        True if the string is a palindrome, False otherwise.
    """
    # Convert the string to lowercase and remove non-alphanumeric characters
    cleaned_string = ''.join(c.lower() for c in string if c.isalnum())

    # Compare the cleaned string with its reversed version
    return cleaned_string == cleaned_string[::-1]

# Get input from the user
user_input = input("Enter a string: ")

# Check if the input is a palindrome
if is_palindrome(user_input):
    print(user_input, "is a palindrome.")
else:
    print(user_input, "is not a palindrome.")