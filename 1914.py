qt=int(input())

for i in range(qt):
    jogadores=input().split()
    nome1=str(jogadores[0])
    escolha1=str(jogadores[1])
    nome2 = str(jogadores[2])
    escolha2 = str(jogadores[3])

    numeros=input().split()
    numerosJ1=int(numeros[0])
    numerosJ2=int(numeros[1])

    if escolha1=="PAR" and escolha2=="IMPAR":
        if (numerosJ1+numerosJ2)%2==0:
            print(nome1)
        else:
            print(nome2)
    if escolha1 == "IMPAR" and escolha2 == "PAR":
        if (numerosJ1 + numerosJ2) % 2 == 0:
            print(nome2)
        else:
            print(nome1)




