def count_digits(n):
    count = 0
    
    while n != 0:
        n = n // 10
        count += 1
        
    return count


# Example usage
n = 12345
result = count_digits(n)

print("Number of digits:", result)
