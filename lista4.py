'''

Faça um programa que leia um vetor de 10 caracteres minúsculos
e diga quantas consoantes foram lidas
'''
char=[]
vogais=["a","e","i","o","u"]
cont=0
for i in range(1,11):
    letra=input("Digite dez letras: ").lower()
    char.append(letra)
    if letra in vogais:
        cont=cont+1
print(cont)