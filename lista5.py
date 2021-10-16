'''

Faça um programa que percorra duas listas e gere uma terceira com os
 elementos das duas primeiras
'''
lista1=[]
lista2=[]
##lista3=lista1+lista2
for numero in range(1,6):
    numero=int(input("Digite os cinco numeros "))
    lista1.append(numero)
for numero in range(1,6):
    numero=int(input("Digite mais cinco numeros "))
    lista2.append(numero)
lista3=lista1+lista2
print(lista3)