def string(str1):
    lowercase = ''
    uppercase = ''
    
    
    for char in str1:
        if char.islower():  
            lowercase += char
        elif char.isupper():  
            uppercase += char
    
    
    return lowercase + uppercase

str1 = "PyNaTive"
result =string(str1)
print(result) 
