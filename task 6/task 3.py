numbers = [1, 2, 3, 4, 5, 6, 7]

res = []
for i in numbers:
    res.append(i * i)
print(res)


numbers = [1, 2, 3, 4, 5]


x = list(map(lambda x: x**2, numbers))


print(x)
