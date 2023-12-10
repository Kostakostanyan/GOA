def triangle(a,b,c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False 
    
a = input("a gverdi: ")
b = input("b gverdi: ")
c = input("c gverdi: ")

if triangle(a,b,c):
    print("shedgeba samkutxedi")
else:
    print("ar shedgeba")