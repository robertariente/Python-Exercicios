n= int(input())

alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(n):
    letras=input()
    pulos=int(input())
    novaPalavra=""

    for j in range(len(letras)):
        posicao=alfabeto.find(letras[j])
        numeroPosicao=posicao-pulos
        if numeroPosicao<0:
            novaPosicao=len(alfabeto)+numeroPosicao
            novaPalavra = novaPalavra + alfabeto[novaPosicao]

        else:
            novaPosicao=numeroPosicao
            novaPalavra=novaPalavra+alfabeto[novaPosicao]
    print(novaPalavra)





