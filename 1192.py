#subprograma
def jogoPaula(num1,letra,num2):
    global resposta
    if num1==num2:
        resposta=num1*num2
    elif letra in ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","X","Z","W","Y"]:
        resposta=num2-num1
    elif letra in ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","z","w","y"]:
        resposta= num1+num2

#programa
casos=int(input())
for i in range(casos):
    n=input()
    num1=int(n[0])
    letra=str(n[1])
    num2=int(n[2])
    jogoPaula(num1,letra,num2)

    print(resposta)