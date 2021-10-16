ano_nasc=int(input("Digite o ano de nascimento: "))
ano_atual=int(input("Digite o ano atual: "))
idade=ano_atual-ano_nasc
if idade<=9:
    print("Mirim!")
elif idade>9 and idade<=14:
    print("Infantil!")
elif idade>14 and idade<=19:
    print("Junior!")
elif idade==20:
    print("Senior")
else:
    print("Master!")
