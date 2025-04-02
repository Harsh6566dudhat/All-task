input_str = "PYnative29@#8496"
total = 0
count = 0
for char in input_str:
    if char.isdigit():
        total += int(char)
        count += 1

avg = total / count
print("Sum is:", total, "Average is ", avg)
