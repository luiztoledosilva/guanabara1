soma=0
for i in range(1,7):
    n=int(input("Digite o %dº inteiro: " %i))
    if n%2==0:
        soma += n
print("Soma dos pares = {} ".format(soma))
    
