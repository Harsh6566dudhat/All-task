
l1 = [1, 2, 3, 4, 5, 6, 7, 8]
l2 = [10, 20, 30, 40, 50, 60, 70, 80]


l3 = []


index = 0  
for element in l1:
    if index % 2 == 1:  
        l3.append(element)
    index += 1  


index = 0 
for element in l2:
    if index % 2 == 0: 
        l3.append(element)
    index += 1  


print("Result list:", l3)
