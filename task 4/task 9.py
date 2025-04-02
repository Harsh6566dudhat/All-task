def find_max(n):
    max_value = 0  
    for num in n:
        if num > max_value:
            max_value = num
    return max_value

n = [1, 2, 3, 4, 5, 6]
result = find_max(n)
print(result)
    