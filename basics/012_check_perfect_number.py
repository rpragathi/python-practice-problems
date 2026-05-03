def is_perfect(n):
    if n < 2:
        return False

    total = 1
    i = 2

    while i < n:   
        if n % i == 0:
            total += i
        i += 1

    return total == n


print(is_perfect(6))  
