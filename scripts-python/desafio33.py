a=int(input("Digite o primeiro numero inteiro A: "))
b=int(input("Digite o segundo numero inteiro B: "))
c=int(input("Digite o terceiro numero inteiro C: "))
###verificar o A:
if a>b and a>c:
    print("O maior numero é A: {} ".format(a))
##verificar o B:
if b>a and b>c:
    print("O maior numero é B: {} ".format(b))
###verificar o C:
if c>a and c>b:
    print("O maior numero é C: {} ".format(c))
