def third_largest(arr):
    """
    Finds the third largest distinct element in an array

    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    first = second = third = float('-inf')

    for num in arr:
        if num > first:
            third = second
            second = first
            first = num

        elif first > num > second:
            third = second
            second = num

        elif second > num > third:
            third = num

    if third == float('-inf'):
        return None  
    return third



arr = [10, 5, 20, 8, 20, 3]
print(third_largest(arr))
