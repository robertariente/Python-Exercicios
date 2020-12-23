
def formaTriangulo(x,y,z,w):

    if x<y+z and y<x+z and z<x+y:
        print("S")
    elif x<y+w and y<x+w and w<y+x:
        print("S")
    elif x < z + w and z < x + w and w < z + x:
        print("S")
    elif y < w + z and w < y + z and z < y + w:
        print("S")
    else:
        print("N")

    return None

#programa
numeros = input().split()
numeros1=int(numeros[0])
numeros2=int(numeros[1])
numeros3=int(numeros[2])
numeros4=int(numeros[3])

x=formaTriangulo(numeros1,numeros2,numeros3,numeros4)


