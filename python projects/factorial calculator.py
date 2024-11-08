# Function to compute factorial iteratively
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Function to compute factorial recursively
def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Take a single integer input from the user
num = int(input("Enter an integer: "))

# Calculate factorial using iteration and recursion
iterative_result = factorial_iterative(num)
recursive_result = factorial_recursive(num)

# Print both results
print(f"Iterative factorial of {num} is: {iterative_result}")
print(f"Recursive factorial of {num} is: {recursive_result}")
