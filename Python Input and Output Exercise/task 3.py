def octal(n):
    octal_number = ""
    
    while n > 0:
        remainder = n % 8  
        octal_number = str(remainder) + octal_number  
        n //= 8  

    print(f"The octal representation is: {octal_number}")


octal(25)
octal(100)
octal(255)
