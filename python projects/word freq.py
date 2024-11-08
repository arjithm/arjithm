import string

def word_frequency_counter(text):
    """Counts the frequency of words in a given text.

    Args:
        text: The input text.

    Returns:
        A dictionary containing word frequencies.
    """

    # Preprocess the text:
    text = text.lower()  # Convert to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    words = text.split()  # Split into words

    # Count word frequencies
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    return word_count

# Example usage:
text = "This is a sample text. This text is for testing word frequency counting. Punctuation and capitalization should be ignored."
word_counts = word_frequency_counter(text)

# Print the results
for word, count in word_counts.items():
    print(f"{word}: {count}")