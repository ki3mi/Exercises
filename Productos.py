prendas = {
1: [0, 40, 0],
2: [0, 100, 0],
3: [0, 35, 0],
4: [0, 80, 0]}

monto = 0
total = 0
y = 0

while(y != 1):
    print("Seleccione el código de producto que desee")
    print("""
    PRODUCTOS           CÓDIGO          PRECIO
    POLO                1               S/.40
    PANTALON            2               S/.100    
    CAMISA              3               S/.35
    POLERA              4               S/.80""")
    x = int(input("Ingrese el código del producto que quiera comprar: "))
    cant = int(input("Ingrese la cantidad de prendas que desea comprar: "))
    prendas[x][2] += cant
    for i in prendas:
        if(i == x):
            monto = prendas[i][2] * prendas[i][1]
            prendas[i][0] = monto
            break
    y = int(input("""
    Precione 1 si ya terminó
    Precione cualquier número si desea continuar
    :> """))
for u in prendas:
    total += prendas[u][0]
print("Monto a pagar: "+ str(total))