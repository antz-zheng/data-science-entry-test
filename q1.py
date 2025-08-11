def swap(x, y):
 
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1
  
    x, y = y, x
    
    # Print swapped values
    print("Swapped values: x =", x, ", y =", y)

swap("Apple", 10)  
swap(9, 17)     
