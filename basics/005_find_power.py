
## Problem
Given two integers `base` and `exponent`, compute the value of:

base^exponent

---


## Method
Power means multiplying the base repeatedly.

base^exponent = base × base × base ... (exponent times)

We can compute this by multiplying the base inside a loop.
---
def power(base, exponent):
    result = 1

    for i in range(exponent):
        result = result * base

    return result


base = 2
exponent = 5

result = power(base, exponent)

print("Power:", result)
