import random
user=int(input("Digite um numero inteiro entre 0 e 5: "))
comp=random.randint(0,5)
if user == comp:
    print("O usuario venceu")
else:
    print("O usuario perdeu")
print("Numero usuario: {} ".format(user))
print("Numero computador: {} ".format(comp))
