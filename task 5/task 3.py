s1 = "America"
s2 = "Japan"


first_char_s1 = s1[0]  
middle_char_s1 = s1[len(s1)//2]  
last_char_s1 = s1[-1]  

first_char_s2 = s2[0] 
middle_char_s2 = s2[len(s2)//2] 
last_char_s2 = s2[-1]  


new_string = first_char_s1 + first_char_s2 + middle_char_s1 + middle_char_s2 + last_char_s2


print(new_string)
