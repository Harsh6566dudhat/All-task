def count_chars_digits_symbols(str1):
    char_count = 0
    digit_count = 0
    symbol_count = 0
    
    
    for char in str1:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':  
            char_count += 1
        elif '0' <= char <= '9':  
            digit_count += 1
        else:  
            symbol_count += 1
    
    return char_count, digit_count, symbol_count


str1 = "P@#yn26at^&i5ve"
chars, digits, symbols = count_chars_digits_symbols(str1)

print("Chars =", chars)
print("Digits =", digits)
print("Symbols =", symbols)