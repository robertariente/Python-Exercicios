n=int(input())

dentro=0
fora=0

for i in range(n):
    x=int(input())
    if x in range (10,20):
        dentro=dentro+1
    else:
        fora=fora+1

print("%d in"%dentro)
print("%d out"%fora)