def rotate(arr, k):
    """
    Rotate array to the right by k steps
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    n = len(arr)
    k = k % n
    def reverse(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)
    return arr
print(rotate([1,2,3,4,5], 2))  
