n = 7

start = 2
sum = 0


for i in range(0, n):
    print(start, end="+")
    sum = sum + start
    start = start * 10 + 2
print("\nSum of above series is:", sum)
