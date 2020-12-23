tempo = input().split()
hora1 = int(tempo[0])
minuto1 = int(tempo[1])
hora2 = int(tempo[2])
minuto2 = int(tempo[3])

if hora1 == hora2 and minuto1 == minuto2:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")

else:
    hora_jogo = hora2 - hora1
    minuto_jogo = minuto2 - minuto1              # 19:10 as 19:20
                                                    # 07:07 a 07:06
    if hora2 <= hora1:
        if minuto1<=minuto2:
            hora_jogo = hora_jogo
        else:
            hora_jogo = hora_jogo + 24


    if minuto2 < minuto1:
        minuto_jogo = minuto_jogo + 60
        hora_jogo = hora_jogo - 1

    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (hora_jogo, minuto_jogo))