numLinha=int(input())
operacao=str(input())

matriz=[]

for i in range(12):
    linha=[]
    for j in range(12):
        numero=float(input())
        linha.append(numero)
    matriz.append(linha)

resultado=0
for k in range(12):
    resultado=resultado+matriz[numLinha][k]

if operacao=="S":
    print(resultado)

else:
    print(resultado/12)