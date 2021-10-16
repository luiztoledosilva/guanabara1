"""
usando laço for - imprimindo numero par

"""
##x=0
fim=int(input("Digite o ultimo numero a ser imprimido: "))
for n in range(0,fim+1):
    if n%2==0:
        print(n, end=' ')
print(n)

