'''

Escreva um programa que pergunte a velocidade do carro de um usuário.
Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado.
Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h
'''

def multa(velocidade):
    if velocidade>=80:
        conta=(velocidade-80)*5
        print("O valor da multa foi R${:.2f} " .format(conta))
    else:
        ##conta=0
        print("O valor da multa foi 0")
v=float(input("digite a velocidade percorrida por km/h:  "))
multa(v)