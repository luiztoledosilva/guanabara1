##import random
from random import randint    
comp=randint(0,10)
print("Tente acertar um numero de 0 a 10: ")
acertou = False
palpites=0
##comp=random.randint(0,10)
while not acertou:
    jogador=int(input("Qual é o seu palpite? "))
    palpites += 1
    if jogador == comp:
        acertou = True
    else:
        if jogador<comp:
            print("Mais...vai tentanto!")
        else:
            print("Menos...vai tentando!")
        
print("Voce acertou com {} palpites ".format(palpites))
    
    

