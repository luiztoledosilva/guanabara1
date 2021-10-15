numero=(int(input("Digite um numero: ")),
        int(input("Digite um numero: ")),
        int(input("Digite um numero: ")),
        int(input("Digite um numero: ")))
print(f"Voce digitou os valors {numero}")
print(f"O valor 9 apareceu {numero.count(9)} vezes ")
if 3 in numero:
    print(f"O valor 3 apareceu na posicao {numero.index(3)+1}")
else:
    print("O valor 3 nao apareceu na lista")
print("Os valores pares digitados foram ")
for n in numero:
    if n%2==0:
        print(n, end=' ')
