def grados(faren:int):
    return (int((faren-32)*5/9))
faren=int(input("Dime los grados farenheit "))
print("La conversión a grados Celsius es",grados(faren))