def power1(base,power):
    prod = 1
    num = power

    while num > 0:
        prod = prod * base
        num = num-1
    print(base,power,prod)    
        
power1(5,4)