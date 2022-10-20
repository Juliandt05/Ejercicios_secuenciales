import math

def hipotri (cat1:int,cat2:int):
    return (int(math.sqrt(cat1*cat1+cat2*cat2)))
    
cat1 = int(input("Dime el primer cateto del triangulo "))
cat2 = int(input("Dime el segundo cateto del triangulo "))
hipo = hipotri (cat1,cat2)
print("La hipotenusa es",hipo)