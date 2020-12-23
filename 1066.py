a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())

impar=0
par=0
positivo=0
negativo=0

if a>0:
    positivo=positivo+1
elif a<0:
    negativo=negativo+1
if a%2==0:
    par=par+1
else:
    impar=impar+1

if b>0:
    positivo=positivo+1
elif b < 0:
    negativo=negativo+1
if b%2==0:
    par=par+1
else:
    impar=impar+1

if c>0:
    positivo=positivo+1
elif c < 0:
    negativo=negativo+1
if c%2==0:
    par=par+1
else:
    impar=impar+1

if d>0:
    positivo=positivo+1
elif d < 0:
    negativo=negativo+1
if d%2==0:
    par=par+1
else:
    impar=impar+1

if e>0:
    positivo=positivo+1
elif e < 0:
    negativo=negativo+1
if e%2==0:
    par=par+1
else:
    impar=impar+1

print("%d valor(es) par(es)"%par)
print("%d valor(es) impar(es)"%impar)
print("%d valor(es) positivo(s)"%positivo)
print("%d valor(es) negativo(s)"%negativo)