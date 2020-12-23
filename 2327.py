n= int(input())
matriz=[]
for j in range(n):
    numlinhas=input().split()
    linha = []
    for i in range(n):
        linha.append(numlinhas[i])
    matriz.append(linha)

somaDiagonal1=0
for k in range(n):
    somaDiagonal1=somaDiagonal1+int(matriz[k][k])

totalLinhas = []
totalColunas = []
for l in range(n):
    somaLinha = 0
    somaColuna = 0
    for m in range(n):
        somaLinha=somaLinha+int(matriz[l][m])
        somaColuna = somaColuna + int(matriz[m][l])
    totalLinhas.append(somaLinha)
    totalColunas.append(somaColuna)

somaDiagonal2 = 0
for o in range(n):
    somaDiagonal2=somaDiagonal2+int(matriz[o][n-1-o])

for i in range (n-1):
    if totalLinhas[i]==totalLinhas[i+1]:
        linha=totalLinhas[0]
    else:
        linha=-1

for i in range (n-1):
    if totalColunas[i]==totalColunas[i+1]:
        coluna=totalColunas[0]
    else:
        coluna=-1

if somaDiagonal1 == somaDiagonal2 == coluna == linha:
    print(linha)
else:
    print(-1)
