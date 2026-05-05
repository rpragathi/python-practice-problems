def rotate(arr, k, direction):
    n = len(arr)
    k %= n

    def rev(l, r):
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

    if direction == "right":
        rev(0, n - 1)
        rev(0, k - 1)
        rev(k, n - 1)

    elif direction == "left":
        rev(0, k - 1)
        rev(k, n - 1)
        rev(0, n - 1)

    return arr


print(rotate([2, 3, 4], 1, "left"))  
print(rotate([2, 3, 4], 1, "right"))  
