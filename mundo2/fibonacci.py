termo=int(input("Digite o numero de termos da frequencia de fibonacci: "))
n1, n2 = 0, 1
cont=0
if termo<0:
    print("Termo positivo!!")
elif termo==1:
    print(f"frequencia de fibonacci {termo}")
    print(n1)
else:
    print("Frequencia de fibonacci: ")
    while cont<termo:
        print(n1)
        num=n1+n2
        n1=n2
        n2=num
        cont +=1
##atualizacao do termo da fibonacci
