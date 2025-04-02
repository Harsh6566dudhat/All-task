def Product(n1,n2):
    Product = n1*n2
    if Product <= 1000:
        return Product
    else:
        return n1+n2
    
print(Product(20,30))
print(Product(40,30))