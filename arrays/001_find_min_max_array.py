def find_min_max(arr):
    """
    Finds minimum and maximum element in an array

    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    if not arr:
        return None, None

    min_val = arr[0]
    max_val = arr[0]

    for num in arr:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num

    return min_val, max_val


arr = [3, 5, 1, 8, 2]
print(find_min_max(arr))
