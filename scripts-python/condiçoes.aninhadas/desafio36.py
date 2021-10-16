casa=float(input("Valor da casa R$ "))
salario=float(input("Salario R$ "))
anos=int(input("Quantos anos de finaciamento: "))
prestacão=casa/(anos*12)
minimo=salario*30/100
##print("O valor da prestaçao mensal sera de R${:.2f} ".format(prestacão))
print("Para pagar uma casa de R${:.2f} em {} anos".format(casa, anos), end=' ')
print("a prestação mensal sera = R${:.2f}".format(prestacão))
if prestacão <=minimo:
    print("Emprestimo pode ser concedido")
else:
    print("Emprestimo nao pode ser concedido")


  
