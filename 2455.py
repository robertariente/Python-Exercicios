numeros = input().split()
p1= int(numeros[0])
c1= int(numeros[1])
p2= int(numeros[2])
c2= int(numeros[3])

lado1=p1*c1
lado2=p2*c2

if lado1==lado2:
    print(0)

elif lado1>lado2:
    print(-1)

else:
    print(+1)
