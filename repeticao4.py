'''

Ler vários números e informar quantos números entre 100 e 200 foram digitados.
Quando o valor 0 (zero) for lido, o programa deve cessar sua execução
'''

x = 1
numero = 0
cont=0
while numero >= 0:
    numero = int(input("%dº  Digite o número: " % x))
    x += 1
    if numero>=100 and numero<=200:
        cont=cont+1
print(cont)