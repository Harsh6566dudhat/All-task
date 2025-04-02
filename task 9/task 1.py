def reverse_tuple(tup):
    reversed_tup = ()  
    for i in range(len(tup) - 1, -1, -1):  
        reversed_tup += (tup[i],) 
    return reversed_tup


tuple1 = (10, 20, 30, 40, 50)
result = reverse_tuple(tuple1)
print(result)  
