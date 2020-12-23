n=int(input())

for i in range(n):
    x=int(input())

    if x==0:
        print("NULL")

    elif x!=0:
        if x>0:
            pn = "POSITIVE"
        else:
            pn= "NEGATIVE"

        if x%2==0:
            pi= "EVEN"
        else:
            pi= "ODD"

        print(pi,pn)
