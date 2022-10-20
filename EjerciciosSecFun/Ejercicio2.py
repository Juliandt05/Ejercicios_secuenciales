base=0
alt=0

def arearec (base:int,alt:int):
    return (int((base*alt)))
    
base = int(input("Dime la base del rectangulo "))
alt = int(input("Dime la altura del rectángulo "))
area = arearec(base,alt)
print("El área del rectangulo es",area)

def perirec (base:int,alt:int):
    return (int(base*2+alt*2))

peri= perirec(base,alt)
print("El perímetro del rectangulo es",peri)