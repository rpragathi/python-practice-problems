def sqrt_integer(n):
    if n < 2:
        return n

    low = 1
    high = n
    ans = 0

    while low <= high:
        mid = (low + high) // 2

        if mid * mid == n:
            return mid
        elif mid * mid < n:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    return ans
