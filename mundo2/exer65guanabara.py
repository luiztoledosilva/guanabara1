resposta='S'
num=0
quantidade=0
while resposta in'Ss':
    num=int(input("digite um numero "))
    quantidade +=1
    if quantidade==1:
        maior=menor=num
    else:
        if num>maior:
            maior=num
        if num<menor:
            menor=num
    resposta=input("Deseja continuar?[s/n]: ").strip().upper()[0]
print(maior)
print(menor)
