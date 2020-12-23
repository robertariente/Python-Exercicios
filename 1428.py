t=int(input())

for i in range(t):
    numeros=input().split()
    n=int(numeros[0])
    m = int(numeros[1])
    sonares = (n//3)*(m//3)
    print(sonares)
