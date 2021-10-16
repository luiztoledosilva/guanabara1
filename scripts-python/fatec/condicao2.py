"""
Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa. O programa deve perguntar
o valor da casa a comprar, o salário e a quantidade de anos a pagar.
O valor da prestação mensal não pode ser superior a 30% do salário.
Calcule o valor da prestação como sendo o valor da casa
a comprar dividido pelo número de meses a pagar

"""

sal=float(input("Digite o valor do seu salário R$ "))
casa=float(input("Digite o valor da casa R$ ")) 
quant=int(input("Digite a quantidade de prestacao(Meses): "))
prestacao=casa/quant
valor=(prestacao/sal)*100
if valor>30:
    print("Seu emprestimo nao foi aprovado, a prestacao ultrapassa 30% do salario conforme abaixo")
    
else:
    print("Seu emprestimo foi aprovado")
print("Valor da prestacao R${:.2f} ".format(prestacao))
print("A porcentagem da prestacação em relação ao seu salário eh igual {:2f} ".format(valor))
