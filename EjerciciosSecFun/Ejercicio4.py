num1=0
num2=0

def suma(num1:int,num2:int):
    return(num1+num2)
def resta(num1:int,num2:int):
    return(num1-num2)
def multi(num1:int,num2:int):
    return(num1*num2)
def divi(num1:int,num2:int):
    return(num1/num2)

num1=int(input("Dime el número 1 "))
num2=int(input("Dime el número 2 "))

print("La suma es",suma(num1,num2))
print("La resta es",resta(num1,num2))
print("La multiplicación es",multi(num1,num2))
print("La división es",divi(num1,num2))