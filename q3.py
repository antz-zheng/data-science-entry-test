def update_dictionary(dct, key, value):

    if not isinstance(dct, dict):
        raise TypeError("dct must be a dictionary")

    if key in dct:
        print(f"Original value for '{key}': {dct[key]}")
    
    dct[key] = value
    return dct

# Task 2
print(update_dictionary({}, "name", "Alice"))
print(update_dictionary({"age": 25}, "age", 26))
