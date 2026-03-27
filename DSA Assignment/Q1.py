def factorial_naive(n: int) -> int:
    if n <= 1:
        return 1
    else:
        return n * factorial_naive(n-1)

def factorial_memoized(n) -> int:
    global memo_factorial
    if memo_factorial[n] != -1: 
        return memo_factorial[n]
    elif n <= 1: 
        return 1
    else:
        memo_factorial[n] = n * factorial_memoized(n-1)
        return memo_factorial[n]

def fibonacci_naive(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fibonacci_naive(n-1) + fibonacci_naive(n-2)

def fibonacci_memoized(n) -> int:
    global memo_fibonacci
    if memo_fibonacci[n] != -1: 
        return memo_fibonacci[n]
    elif n <= 1: 
        memo_fibonacci[n] = n
        return n
    else:
        memo_fibonacci[n] = fibonacci_memoized(n-1) + fibonacci_memoized(n-2)
        return memo_fibonacci[n]

memo_factorial = []
memo_fibonacci = []

# Main method
def main():
    global memo_factorial
    global memo_fibonacci
    
    # Input
    n = int(input("Enter a positive integer: "))
    
    # Input Validation
    while (n < 0):
        n = int(input("Error, Enter a positive integer: "))
    
    # Initialise lists
    memo_fibonacci = [-1] * (n+1)
    memo_factorial = [-1] * (n+1)
    
    # Print Factorial and Fibonacci
    print(f"Factorial of {n} using naive approach is {factorial_naive(n)}")
    print(f"Factorial of {n} using memoized approach is {factorial_memoized(n)}")
    print(f"Fibonacci term at {n} using naive approach is {fibonacci_naive(n)}")
    print(f"Fibonacci term at {n} using memoized approach is {fibonacci_memoized(n)}")

if __name__ == "__main__":
    main()
