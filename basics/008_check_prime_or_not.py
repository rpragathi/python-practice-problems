def is_prime(n):

     """
    Checks whether a number is prime

    Time Complexity: O(√n)
    Space Complexity: O(1)

    Explanation:
    - Only checks divisibility up to square root of n
    - Skips even numbers 
    
    """
    if n <= 1:
        return False
    
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2  
    return True

