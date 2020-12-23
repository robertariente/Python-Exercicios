x=int(input())
y=int(input())

if x<=y:
    for n in range (x+1,y):
        if n%5==2 or n%5==3:
            print(n)

elif y<=x:
    temp=x
    x=y
    y=temp
    for n in range (x+1,y):
        if n%5==2 or n%5==3:
            print(n)
