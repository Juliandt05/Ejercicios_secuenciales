mon2=int(input("Cuantas monedas tienes de 2€" ))
mon1=int(input("Cuantas monedas tienes de 1€" ))
mon50=int(input("Cuantas monedas tienes de 50 cent" ))
mon20=int(input("Cuantas monedas tienes de 20 cent" ))
mon10=int(input("Cuantas monedas tienes de 10 cent" ))
euro50=0
euro20=0
euro10=0
cent=0

if mon50>=2:
    euro50=mon50/2
    mon50=mon50%2*50
else:
    mon50=mon50*50
if mon20>=5:
    euro20=mon20/5
    mon20=mon20%5*20
else:
    mon20=mon20*20
if mon10>=10:
    euro10=mon10/10
    mon10=mon10%10*10
else:
    mon10=mon10*10
    

print("El dinero que tienes es",int(mon2+mon1+euro50+euro20+euro10),"€ y",mon50+mon20+mon10,"céntimos")