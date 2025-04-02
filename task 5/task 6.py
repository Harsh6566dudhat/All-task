def merge_strings(s1, s2):
    s3 = ''
    i = 0
    j = len(s2) - 1

   
    while i < len(s1) and j >= 0:
        s3 += s1[i] 
        s3 += s2[j]  
        i += 1
        j -= 1

   
    while i < len(s1):
        s3 += s1[i]
        i += 1

    
    while j >= 0:
        s3 += s2[j]
        j -= 1

    return s3


s1 = "Abc"
s2 = "Xyz"
result = merge_strings(s1, s2)
print("Expected Output:", result)
