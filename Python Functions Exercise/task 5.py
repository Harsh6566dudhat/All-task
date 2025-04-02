
def outer(a, b):
    

    
    def addition(a, b):
        return a + b

    add = addition(a, b)
 
    return add + 5

result = outer(5, 100)
print(result)
