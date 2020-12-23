x=int(input())

i=1
for i in range(x):
    palavras=input().split()
    palavra1=palavras[0]
    palavra2=palavras[1]

    if len(palavra1)<len(palavra2):
        palavraMenor=palavra1
        palavraMaior=palavra2
    else:
        palavraMenor=palavra2
        palavraMaior=palavra1

    primeiraMetade = ""
    for j in range(len(palavraMenor)):
        primeiraMetade= primeiraMetade + palavra1[j] + palavra2[j]

    segundaMetade=palavraMaior[len(palavraMenor):len(palavraMaior)]

    novaPalavra=primeiraMetade+segundaMetade

    print(novaPalavra)





