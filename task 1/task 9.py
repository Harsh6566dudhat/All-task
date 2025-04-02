def palindrome(number):
    
    original_num = number
    
    
    rev = 0
    while number > 0:
        digit = number % 10
        rev = (rev * 10) + digit
        number = number // 10

    
    if original_num == rev:
        print("Given number palindrome")
    else:
        print("Given number is not palindrome")

palindrome(121)
palindrome(125)