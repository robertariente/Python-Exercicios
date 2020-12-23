def analisaNumeros(numeros):
    cres =0
    decres=0
    for i in range(4):
        if numeros[i]<numeros[i+1]:
            cres=cres+1

        elif numeros[i]>numeros[i+1]:
            decres=decres+1


    if cres == 4:
        print("C")
    elif decres == 4:
        print("D")
    else:
        print("N")

#programa
cartas = input().split()
numeros=[]
for i in range(5):
    numeros.append(int(cartas[i]))
crescDec = analisaNumeros(numeros)

