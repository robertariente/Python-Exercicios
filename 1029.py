#subprogramas:
def fib(x):
    global chamada
    chamada=chamada+1
    if x <= 1:
        return x
    else:
        return fib(x-1) + fib(x-2)

#programaPrincipal:
Nteste=int(input())

for n in range(Nteste):
    x=int(input())
    chamada=0
    y=fib(x)
    if x>=2:
        chamada=chamada-1
    print("fib(%d) = %d calls = %d"%(x,chamada,y))