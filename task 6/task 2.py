l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]
l3 = []
i = 0
j = 0


while i < len(l1) and j < len(l2):
    l3.append(l1[i])  
    l3.append(l2[j])  
    i = i + 1
    j = j + 1

print("List 1:", l1)
print("List 2:", l2)
print("Combined List:", l3)
    