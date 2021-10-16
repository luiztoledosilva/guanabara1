'''

Entrar com números enquanto forem positivos e imprimir quantos números foram digitados
'''


x = 1
numero = 0
cont=0
while numero >= 0:
    numero = int(input("%dº  Digite o número: " % x))
    x += 1
    if numero>0:
        cont=cont+1
print(cont)

