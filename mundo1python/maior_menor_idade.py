from datetime import date
atual=date.today().year
contmaior=0
contmenor=0
for pessoas in range(1,8):
   nasc=int(input("Digite o ano de nascimento: "))
   idade=atual-nasc
   if idade>=18:
      contmaior += 1
   else:
      contmenor += 1
print(f" maior = {contmaior}")
print(f" menor = {contmenor} ")