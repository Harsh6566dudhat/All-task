def list(num):
    first = num[0]
    last = num[-1]

    if first == last:
        return True
    else:
        return False
    
n = [10,20,30,40,10]
print(list(n))  
n = [10,20,30,40,20]
print(list(n))    

    