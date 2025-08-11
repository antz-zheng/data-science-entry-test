def check_divisibility(num, divisor):

    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
        raise TypeError("Both num and divisor must be numeric")
    
    if divisor == 0:
        raise ValueError("divisor cannot be zero")
    
    return num % divisor == 0

print(check_divisibility(10, 2))  
print(check_divisibility(7, 3))   
