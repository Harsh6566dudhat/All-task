print(" current and previous number and  sum in a range(20)")
prev_num = 0


for i in range(1, 21):
    sum = prev_num + i
    print("Current Number", i, "Previous Number ", prev_num, " Sum: ", sum)
   
    prev_num = i
