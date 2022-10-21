def comiprod(venta1:int,venta2:int,venta3:int):
    return(venta1*0.1+venta2*0.1+venta3*0.1)
def sueldof(sueldo:int,venta1:int,venta2:int,venta3:int):
    return(sueldo+(venta1+venta2+venta3)*0.1)
sueldo=int(input("Dime el valor de tu sueldo "))
venta1=int(input("Dime el valor la primera venta "))
venta2=int(input("Dime el valor la segunda venta "))
venta3=int(input("Dime el valor la tercera venta "))
print("El 10 % de los productos es",comiprod(venta1,venta2,venta3))
print("Tu sueldo total es",sueldof(sueldo,venta1,venta2,venta3))
