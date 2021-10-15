import random

n1=input("Digite o primeiro aluno: ")
n2=input("Digite o segundo aluno: ")
n3=input("Digite o terceiro aluno: ")
n4=input("Digite o quarto aluno: ")
lista=[n1,n2,n3,n4]
escolhido=random.choice(lista)
print("O escolhido foi {} ".format(escolhido))