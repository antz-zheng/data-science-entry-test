def find_first_negative(lst):

    if not isinstance(lst, list):
        raise TypeError("lst must be a list")
    
    index = 0
    while index < len(lst):
        if lst[index] < 0:
            return lst[index]
        index += 1
    
    return "No negatives"

print(find_first_negative([3, 5, -1, 7, -2, 8]))  
print(find_first_negative([2, 10, 7, 0]))   
