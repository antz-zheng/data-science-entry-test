def string_reverse(s):

    if not isinstance(s, str):
        raise TypeError("s must be a string")
    
    return s[::-1]

print(string_reverse("Hello World"))
print(string_reverse("Python"))
