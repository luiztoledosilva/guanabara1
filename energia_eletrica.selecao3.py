'''
) Escreva um programa que calcule o preço a pagar pelo fornecimento de
 energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação:
 R para residências,
 I para indústrias e
C para comércios. Calcule o preço a pagar, de acordo com a tabela a seguir:
'''

def preco(tipo,kwh):
    if tipo=='R'and kwh <=500:
        return kwh * 0.40
    elif tipo=='R' and kwh > 500:
        return kwh * 0.65
    elif tipo=='C' and kwh<=1000:
        return kwh * 0.55
    elif tipo=='C' and kwh>1000:
        return kwh * 0.60
    elif tipo=='I' and kwh<=5000:
        return kwh * 0.55
    elif tipo=='I' and kwh>5000:
        return kwh * 0.60
    else:
        return "Valor invalido!"
escolha=input("Digite R para residencial, C para comercial e I para industrial ").upper()
valor=float(input("Digite o valor do kwh gasto: "))
print("O valor da conta é de R${:.2f} " .format(preco(escolha,valor)))



