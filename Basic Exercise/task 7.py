def counting(statement):
    
    count = 0
    for i in range(len(statement) - 1):
        count += statement[i: i + 4] == 'Emma'
    return count

count = counting("Emma is good developer. Emma is a writer")
print("Emma appeared ", count, "times")