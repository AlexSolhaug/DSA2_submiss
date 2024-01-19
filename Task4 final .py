# Define the recursive function for the Collatz conjecture
def collatz(n):
    # If n is 1, the function returns as the base condition is met
    if n == 1:
        return [1]
    
    # If n is even, the function calls itself with n/2
    if n % 2 == 0:
        return [n] + collatz(n // 2)
    
    # If n is odd, the function calls itself with 3n + 1
    else:
        return [n] + collatz(3 * n + 1)

# Example usage of the function
collatz_sequence = collatz(13)# use any number n>0
print(collatz_sequence)
