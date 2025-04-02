str1 = 'Harsh'
print("Original String is", str1)


res = str1[0]


l = len(str1)

mi = int(l / 2)

res = res + str1[mi]
res = res + str1[l - 1]

print("New String:", res)


def get_middle(str1):
    print("Original String is", str1)

    
    mi = int(len(str1) / 2)

    res = str1[mi - 1:mi + 2]
    print("Middle three chars are:", res)

get_middle("Harshdudhat")
