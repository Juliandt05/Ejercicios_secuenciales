notas1=int(input("Dime la nota de la primera calificación "))
notas2=int(input("Dime la nota de la segunda calificación "))
notas3=int(input("Dime la nota de la tercera calificación "))
examenf=int(input("Dime la calificación del examen final "))
trabf=int(input("Dime la nota del trabajo final "))
print("Tu calificación final es",(notas1+notas2+notas3)/3*0.55+examenf*0.3+trabf*0.15)