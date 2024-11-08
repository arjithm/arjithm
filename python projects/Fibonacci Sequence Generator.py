# Function to generate Fibonacci sequence
def fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)10

        a, b = b, a + b
    return sequence

# Take integer input from the user
n = int(input("Enter the number of terms: "))

# Generate and print the Fibonacci sequence
fib_sequence = fibonacci_sequence(n)
print(", ".join(map(str, fib_sequence)))
