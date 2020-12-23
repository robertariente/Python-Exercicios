n=int(input())

hora=n//3600  #3700, 1 hora
resto_hora=n%3600  #sobra 100

minuto=resto_hora//60 #100/60 = 1
resto_minuto=resto_hora%60  #40

segundo=resto_minuto

print("%d:%d:%d"%(hora,minuto,segundo))
