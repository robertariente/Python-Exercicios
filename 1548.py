#subProg
def trocaNumero(vetor,pos1,pos2):
    temp=vetor[pos1]
    vetor[pos1]=vetor[pos2]
    vetor[pos2]=temp
    return None

def ordena(valores,qt):
    for i in range(qt):
        for j in range(qt-1):
            if valores[j]<valores[j+1]:
                trocaNumero(valores,j,j+i)
    return valores
#prog
n=int(input())
for i in range(n):
    notas=[]
    comparaFila=[]
    nAlunos=int(input())
    nNotas=input().split()
    for j in range(nAlunos):
        notas.append(int(nNotas[j]))
    for l in range(nAlunos):
        comparaFila.append(int(nNotas[l]))
    fila=ordena(notas,nAlunos)

    naoMudaram=0
    for k in range(nAlunos):
        if comparaFila[k]==fila[k]:
            naoMudaram=naoMudaram+1
    print(naoMudaram)



