def find_missing_sum(arr):
    """
    Finds missing number using sum formula

    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    n = len(arr) + 1  # total numbers including missing

    expectedsum = n * (n + 1) // 2
    actualsum = sum(arr)

    return expectedsum - actualsum


print(find_missing_sum([1, 2, 4, 5]))  # 3
