notaValida=False

while notaValida == False:
    n1=float(input())
    if n1<0 or n1>10:
        print("nota invalida")
    else:
        notaValida=True
        nota1=n1

notaValida=False

while notaValida == False:
    n2=float(input())
    if n2<0 or n2>10:
        print("nota invalida")
    else:
        notaValida=True
        nota2=n2

else:
    media=(nota1+nota2)/2
    print("media = %.2f"%media)