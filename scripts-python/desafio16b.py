##num=float(input("Digite um numero flutuante do tipo 5.5555: "))
##print(f'a parte inteira é {num:.0f}')
from math import trunc
num=float(input("Digite um numero flutuante(ou real): "))
print("O valor digitado foi {} e a sua parte inteira {}".format(num, trunc(num)))
