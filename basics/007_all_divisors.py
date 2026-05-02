# Problem 007: Print All Divisors of a Number

Given a positive integer `n`, print all numbers that divide `n` completely.

Example:  
Input: 12  
Output: 1 2 3 4 6 12  

---

Instead of checking all numbers from 1 to n, we only check up to √n.

If a number `i` divides `n`, then both `i` and `n / i` are divisors.

So we collect smaller divisors in one list and corresponding larger divisors in another list.

---

```python
import math

def print_divisors(n):
    small = []
    large = []

    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            small.append(i)

            if i != n // i:
                large.append(n // i)

    for x in small:
        print(x, end=" ")
    for x in reversed(large):
        print(x, end=" ")


# Example usage
n = 12
print_divisors(n)
