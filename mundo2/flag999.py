
num=0
cont=0
soma=0
x=1
while num !=999:
    num = int(input("Digite um numero ou 999 para parar: "))
    if num != 999:
        cont += 1
        soma += num
    x=x+1
print(cont)
print(soma)


