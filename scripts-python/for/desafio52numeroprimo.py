cont=0
n=int(input("Digite um numero p/ descobrir se é primo: "))
for x in range(1,n+1):
    if n%x==0:
        cont += 1
if cont==2:
    print("numero primo!")
else:
    print("O numero nao é primo!")
