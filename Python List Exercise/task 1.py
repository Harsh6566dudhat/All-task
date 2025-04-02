# list1 = [100, 200, 300, 400, 500]
# list1.reverse()
# print(list1)


def rev(l1):
    l2 = []

    for i in range(len(l1)-1,-1,-1):
        l2.append(l1[i])
    return l2    

n = [1,2,3,4,5]
print(rev(n))