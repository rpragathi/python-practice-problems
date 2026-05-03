def find_all_duplicates(arr):
    """
    Finds all duplicate elements in an array

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    traversed_numbers = set()
    duplicates = set()

    for num in arr:
        if num in traversed_numbers:
            duplicates.add(num)
        else:
            traversed_numbers.add(num)

    return list(duplicates)



print(find_all_duplicates([2, 3, 1, 1, 4, 4])) 
