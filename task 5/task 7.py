def string_balance_test(s1, s2):
    sta = True
    for char in s1:
        if char in s2:
            continue
        else:
            sta = False
    return sta


s1 = "Yn"
s2 = "PYnative"
flag = string_balance_test(s1, s2)
print("s1 and s2 are balanced:", flag)

s1 = "Ynf"
s2 = "PYnative"
flag = string_balance_test(s1, s2)
print("s1 and s2 are balanced:", flag)


