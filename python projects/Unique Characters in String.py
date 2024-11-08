def has_unique_characters(input_string):
    # Normalize the string by converting to lowercase and removing spaces
    normalized_string = input_string.lower().replace(" ", "")
    # Use a set to check for unique characters
    unique_chars = set()

    for char in normalized_string:
        if char in unique_chars:
            return False
        unique_chars.add(char)

    return True


# Take input from the user
input_string = input("Enter a string: ")

# Check for unique characters and print the result
if has_unique_characters(input_string):
    print("True")
else:
    print("False")
