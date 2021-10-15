import random

numero=random.randint(1,11)
acertou=0
cont=0
n=int(input("Digite um numero de 1 a 10: "))
while numero != n:
    n = int(input("Digite um numero de 1 a 10: "))
    cont +=1
    if numero==n:
        acertou=n
        print("acertou!")
        print(f"O numero eh {n}")
print(f"foram {cont+1} tentativas")