n= int(input())
numLado = 0

while n != 0:
    for i in range(n):
        dados=input().split()
        ci = int(dados[0])
        vi= int(dados[1])
        numLado = numLado + vi//2
        retangulos=numLado//2
    print(retangulos)
    n= int(input())
    numLado=0




