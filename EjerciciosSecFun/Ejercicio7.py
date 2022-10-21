def minahoras(min:int):
    return int((min/60))
def minamin(min:int):
    return int((min%60))
min=int(input("Dime los minutos "))
print("La conversión de min a horas es",minahoras(min),"horas y",minamin(min))