primeiro=int(input("Digite o primeiro numero: "))
fim=int(input("Digite o ultimo numero: "))
for n in range(primeiro, fim+1):
    print(n)                         ###intervalo do primeiro ao último
print("FIM")
for n in range(primeiro, fim+1,2):
    print(n)                         ###intervalo do primeiro ao último
print("FIM")                               ##com passo
for n in range(fim,primeiro,-1):
    print(n)                         ##intervalo do ultimo ao primeiro 
print("FIM")    



