from datetime import date
atual=date.today().year
nascimento=int(input("Digite o ano de nascimento: "))
idade=atual-nascimento
print(f"Voce tem {idade} em {atual} e nasceu em {nascimento} ")
if idade>18:
    print("Voce já se alistou ou deveria ter se alistado! ")
if idade==18:
    print("Voce está em ano de alistamento!")
elif idade<18:
    print("Voce ainda estara em ano de alistamento!!")
