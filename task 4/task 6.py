def addition(num):
    if num:
        return num + addition(num - 1)
    else:
        return 0

res = addition(100)
print(res)
