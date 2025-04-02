employees = ['Harsh', 'Raj']
defaults = {"designation": 'Developer', "salary": 80000}

res = dict.fromkeys(employees, defaults)
print(res)

