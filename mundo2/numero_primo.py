cont=0
primo=int(input("Digite um número p verificar se é primo: "))
for i in range(1,primo+1):
    if primo%i==0:
        cont=cont+1
if cont==2:
    print("O numero é primo")
else:
    print("O número não é primo")