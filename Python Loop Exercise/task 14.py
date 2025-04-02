num = int(input("enter thr nub:"))

reverse_number = 0

while num > 0:
    reminder = num % 10
    reverse_number = (reverse_number * 10) + reminder
    num = num // 10
print("Revere Number ", reverse_number)