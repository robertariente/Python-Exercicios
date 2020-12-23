n=int(input())

if n == 0:
    fib0=0
    print(fib0)
elif n == 1:
    fib0=0
    fib1=1
    print(fib0, fib1)

else:
    fib0 = 0
    fib1 = 1
    print(fib0,fib1,end=" ")
    for i in range(2,(n-1)):
        fibn = fib0+fib1
        print(fibn, end=" ")
        fib0=fib1
        fib1=fibn
    fibFIM=fib0+fib1
    print(fibFIM)