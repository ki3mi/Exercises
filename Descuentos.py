import random
c = 0
while(c != 1):
    montoCLiente = float(input("ingrese el monto a pagar: "))
    montoTotal = 0

    if(montoCLiente >= 100):
        print("""
    *Usted obtuvo un descuento aleatorio*
    Los siguientes colores determinan el descuento:
    BLANCO  -> 0%
    ROJO    -> 10%
    AZUL    -> 20%
    VERDE   -> 25%
    AMARILLO-> 50%""")
        x = random.randint(1, 5)
        if(x==1):
            print("EL color que obtuvo es BLANCO")
            montoTotal = montoCLiente
        elif(x==2):
            print("El color que obtuvo es ROJO")
            montoTotal = montoCLiente - montoCLiente * 0.1
        elif(x==3):
            print("El color que obtuvo es AZUL")
            montoTotal = montoCLiente - montoCLiente * 0.2
        elif(x==4):
            print("El color que obtuvo es VERDE")
            montoTotal = montoCLiente - montoCLiente * 0.25
        else:
            print("El color que obtuvo es AMARILLO")
            montoTotal = montoCLiente - montoCLiente * 0.5
    else:
        print("Usted no aplica a la promoción")
        montoTotal = montoCLiente
    print("El monto a pagar es de S/." + str(montoTotal))
    c = int(input("""
    Si desea salir presione 1
    si desea continuar presione cualquier número
    :> """))