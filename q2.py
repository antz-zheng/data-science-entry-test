def find_and_replace(lst, find_val, replace_val):

    if not isinstance(lst, list):
        raise TypeError("lst must be a list")
    
    return [replace_val if item == find_val else item for item in lst]

# Task 2
print(find_and_replace([1, 2, 3, 4, 2, 2], 2, 5))
print(find_and_replace(["apple", "banana", "apple"], "apple", "orange"))
