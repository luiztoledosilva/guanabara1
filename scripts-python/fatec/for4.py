cont=0
fim=int(input("Digite o último numero a ser imprimido: "))
for n in range(0, fim+1):
    print(n)
    if n%2==0:
        cont=cont+1
print("a quantidade de numeros pares é igual a {} ".format(cont))
