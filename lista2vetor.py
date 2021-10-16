'''

Faça um programa que leia um vetor de 10 números reais e mostre-os na ordem inversa
'''


L = []""
n=0
x=1
while x<=5:
    n=int(input("Digite 5 numeros "))
    L.append(n)
    x=x+1
    ##L2=L.sort()
    ##L3=L.sort(reverse=True)
#print(L)
print(L[0:5])
print(L.reverse())



