valor=float(input("Digite o valor do produto R$ "))
print("""
       [1] a vista dinheiro 10% de desconto
       [2] no cartao a vista 5% de desconto
       [3] em até 2x - preco normal
       [4] acima de 3x - 20% de juros
""")
opcao=int(input("Digite a opcao: "))
if opcao==1:
    print("O valor sera de R${:.2f}" .format(valor*0.9))
elif opcao==2:
    print("O valor sera de R${:.2f}".format(valor * 0.95))
elif opcao==3:
    print("Sera duas prestacoes de R${:.2f} cada ".format(valor/2))
elif opcao==4:
    prestacao=int(input("Digite o numero de prestacoes "))
    if prestacao<3:
        print("Erro!")
    else:
        valor2=(valor*1.2)/prestacao
        print("cada prestacao tera o valor de R${:.2f} ".format(valor2))

