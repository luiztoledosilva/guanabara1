print("Ano Bissexto: ")
ano=int(input("Digite o ano p/ verificacao: "))
if ano%4==0 or ano%400==0 and not ano%100==0:
    print("O ano é bissexto")
else:
    print("O ano nao é bissexto")
              
