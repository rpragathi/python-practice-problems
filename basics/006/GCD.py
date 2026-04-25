## Problem
Given two positive integers `a` and `b`, find their Greatest Common Divisor (GCD)

The GCD is the largest number that divides both `a` and `b` completely.


## Pattern

Instead of checking all numbers, used the Euclidean Algorithm:

GCD(a, b) = GCD(b, a % b)

We repeatedly reduce the problem until `b == 0`.

At that point:
GCD = a

---

def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a


a = 12
b = 18

result = gcd(a, b)

print("GCD:", result)
