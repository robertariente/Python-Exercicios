n= int(input())
palavra=[]

for i in range(n):
    linha=str(input())
    for j in range(len(linha)):
        if j!=" ":
            palavrateste=[]
            while j!= " " and "":
                palavrateste.append(j)
            palavra.append(palavrateste[0])

            print(palavra)

