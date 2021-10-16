'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
 O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a
 pagar. O valor da prestação mensal não pode ser superior a 30% do salário.
Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar

'''

def emprestimo(valor_casa,salario,qtde_anos):
    prestacao=(valor_casa/qtde_anos)*(qtde_anos/12)
    ##porcentagem=(salario*100)/prestacao
    porcentagem=(prestacao/salario)*100
    print("O valor da prestacao é igual a R${:.2f} " .format(prestacao))
    if porcentagem>30:
        print("Emprestimo negado!")
    else:
        print("Emprestimo concedido!")
    print("Porcentagem de {:.2f} em relacao ao salario " .format(porcentagem))
v1=float(input("Digite o valor da casa R$ "))
v2=float(input("Digite o valor do salario R$ "))
v3=int(input("Digite os anos de prestacao: "))
emprestimo(v2,v2,v3)

