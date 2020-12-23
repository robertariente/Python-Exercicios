def troca(vetor,x,y):
    temp = vetor[x]
    vetor[x]=vetor[y]
    vetor[y]=temp
    return None

def ordenaNumeros(valores):
    for i in range(3):
        for j in range(2):
            if valores[j]>valores[j+1]:
                troca(valores,j,j+1)
    return (valores)

n=input().split()
numeros=[]
num1=int(n[0])
num2=int(n[1])
num3=int(n[2])
numeros.append(num1)
numeros.append(num2)
numeros.append(num3)

ordenado = ordenaNumeros(numeros)
print(ordenado[0])
print(ordenado[1])
print(ordenado[2])
print()
print(num1)
print(num2)
print(num3)