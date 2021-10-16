"""
o programa consiste em colocar na ordem
os alunos na hora de apresentar um trabalho.

"""


#import random
from random import shuffle
a1=input("Digite o nome do primeiro aluno: ")
a2=input("Digite o nome do segundo aluno: ")
a3=input("Digite o nome do terceiro aluno: ")
a4=input("Digite o nome do quarto aluno: ")
alunos=[a1,a2,a3,a4]  ###lista
#escolha=random.choice(alunos)
#print("O aluno escolhido foi {} ".format(escolha))
shuffle(alunos)
print("A ordem de apresentacao sera ")
print(alunos)
