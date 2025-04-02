def rev(st):
    revstr = ""
    for char in st:
        revstr = char + revstr  
    return revstr  


a = "python"
print(rev(a))
