extenso=('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez')
while True:
    num=int(input("Digite um numero entre 1 e 10: "))
    if num>=0 and num<11:
        break
print(f"voce digitou o numero {extenso[num]}")