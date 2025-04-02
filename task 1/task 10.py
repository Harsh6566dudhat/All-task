def merge(l1,l2):
    l3 = []

    for i in l1:
        if i % 2 != 0:
            l3.append(i)

    for i in l2:
        if i % 2 == 0:
            l3.append(i)
    return l3

l1 = [10, 20, 25, 30, 35]
l2 = [40, 45, 60, 75, 90] 
print(merge(l1,l2))                
