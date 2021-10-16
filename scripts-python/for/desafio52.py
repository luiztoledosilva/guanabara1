num=int(input("Digite um numero: "))
for cont in range(1,num+1):
    if num%cont==0:
        print("Numero primo!")
    else:
        print("Nao é numero primo!")
