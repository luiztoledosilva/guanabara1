'''

Escreva um programa que leia um valor em metros e o exiba convertido em milímetros
'''

def conversao(metros):
    milimetros=metros*1000
    print("{} metros é equivalente a {:.2f} milimetros " .format(metros,milimetros))

m=float(input("digite os metros para serem convertidos em milimetros "))

conversao(m)