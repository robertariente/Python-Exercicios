#subprogramas
def refeicoes(alimentos):
    cafe=[]
    cafeVez=input()
    cafe.append(cafeVez)
    if cafe in (alimentos):
        sobra=alimentos-cafe
    else:
        print("CHEATER")
    almoco=[]
    almocoVez= input()
    almoco.append(almocoVez)
    if almoco in (alimentos) and almoco !=cafe:
        jantar=alimentos-almoco-cafe
        print(jantar)
    else:
        print("CHEATER")

#programa
casos=int(input())
alimentos=[]
for n in range(casos):
    dieta=(input())
    for i in range(len(dieta)):
        alimentos.append(dieta[i])
        refeicoes(alimentos)
