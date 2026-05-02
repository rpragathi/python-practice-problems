def is_palindrome_optimized(n):
    """
    Checks palindrome by reversing half the number.

    Time Complexity: O(d)
    Space Complexity: O(1)

    - Compare first half with reversed second half
    """

    # Edge cases
    if n < 0 or (n % 10 == 0 and n != 0):
        return False

    rev = 0

    # Reverse half of the number
    while n > rev:
        rev = rev * 10 + n % 10
        n //= 10

    # For even digits: n == rev
    # For odd digits: remove middle digit → rev // 10
    return n == rev or n == rev // 10
