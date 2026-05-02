def is_armstrong(n):
    """
    Checks whether a number is an Armstrong number.

    Time Complexity: O(d) where d is number of digits
    Space Complexity: O(1)

    Where d = number of digits

    Explanation:
    - Extracts each digit
    - Raises it to power of total digits
    - Sums and compares with original number
    """

    num_str = str(n)
    k = len(num_str)

    total = 0

    for digit in num_str:
        total += int(digit) ** k
    return total == n

print(is_armstrong(153))
