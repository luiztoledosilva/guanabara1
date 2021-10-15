"""

Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo,
 qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
"""
soma=0
media=0
maisvelho=''
maior=0
for i in range(1,5):
    print("%dªpessoa" %i)
    nome=input("Digite o nome da pessoa: ").strip().title()
    sexo=input("Digite o sexo da pessoa: M para masculino e F para feminino: ").upper()
    idade=int(input("Digite a idade da pessoa: "))
    soma=soma+idade
    media=soma/4
    if i==1 and sexo in 'M':
        maisvelho=nome
        maior=idade
    if sexo in 'M' and idade>maior:
        maisvelho = nome
        maior = idade
print(f"A media de idade = {media:.2f}")
print(f"O homem com maior é {maisvelho} com idade de {maior} anos ")