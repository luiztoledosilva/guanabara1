"""
Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa
"""
n1 = float(input("Digite n1: "))
n2 = float(input("Digite n2: "))
opcao=0
while opcao !=5:


    opcao = int(input("Digite a opcao: "))
    if opcao==1:
        soma=n1+n2
        print(f"soma= {soma} ")
    elif opcao==2:
        subtracao=n1-n2
        print(f"a subtracao = {subtracao}")
    elif opcao==3:
        if n1>n2:
            maior=n1
            print(f"maior = {maior}")
        elif n2>n1:
            maior=2
            print(f"O maior = {n2}")
        else:
            print("Os numeros sao iguais")
    elif opcao==4:
        n1=float(input("Digite n1: "))
        n2=float(input("Digite n2: "))
    elif opcao==5:
        print("finalizado")
    else:
        print("opcao invalidada!!!")

