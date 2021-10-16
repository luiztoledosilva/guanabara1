cont=0
cont2=0
##idade=0
atual=int(input("Digite o ano atual: "))
for pessoas in range(1,8):
    nasc=(int(input("Digite o ano de nascimento da %dª pessoa: " %pessoas)))
    idade=atual-nasc
    if idade>=18:
          cont += 1
    else:
        cont2 += 1
print("{} sao maiores de idade ".format(cont))
print("{} sao menores de idade ".format(cont2))
