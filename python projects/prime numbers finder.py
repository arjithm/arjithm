def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Take two integers, start and end, as inputs
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Find and print all prime numbers in the given range
prime_numbers = find_primes(start, end)
print(f"Prime numbers between {start} and {end} are: {prime_numbers}")
