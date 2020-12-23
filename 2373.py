n=int(input())
coposQuebrados=0
for i in range(n):
    bandeja=input().split()
    latas=int(bandeja[0])
    copos=int(bandeja[1])

    if latas>copos:
        coposQuebrados=coposQuebrados+copos

print(coposQuebrados)