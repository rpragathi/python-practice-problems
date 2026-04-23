def reverse_number(n):
    reversed_number = 0

    while n != 0:
        last_digit = n % 10
        reversed_number = reversed_number * 10 + last_digit
        n = n // 10

    return reversed_number


n = 1234
result = reverse_number(n)

print("Reversed number:", result)
