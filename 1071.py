x=int(input())
y=int(input())
soma =0

if x<=y:
    for n in range(x+1,y,1):
        if n%2!=0:
            soma=soma+n

elif x>y:
    for n in range (x-1,y,-1):
        if n%2!=0:
            soma=soma+n

print(soma)