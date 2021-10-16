"""
Escreva um programa que pergunte a velocidade
do carro de um usuário.
Caso ultrapasse 80 km/h, exiba uma mensagem dizendo
que o usuário foi multado.
Nesse caso, exiba o valor da multa,
cobrando R$ 5 por km acima de 80 km/h

"""
print("Exer 1 if/else - fatec")
velocidade=float(input("Qual a velocidade do carro: "))
if velocidade>80:
    multa=(velocidade-80)*5
    print("A multa foi de R${:.2f} ".format(multa))
else:
    multa=0
    print("A multa foi de R${:.2f} ".format(multa))
