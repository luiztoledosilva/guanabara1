import random

numero=random.randint(1,6)
##print(numero)
n=int(input("Digite um numero de um a cinco: "))
if n==numero:
    print(f"Numero {n}.O usuario acertou ")
else:
    print(f"O numero {n} é diferente de {numero}, portanto o usuario errou! ")
