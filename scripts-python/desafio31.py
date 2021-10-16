###preco=float(input("Preço da passagem R$ "))
km=float(input("KM viagem: "))
if km<=200:
    print("O preço da viagem foi R${:.2f} ".format(km*0.50))
    print("Um custo de 50 centavos por KM")
else:
    print("O preço da viagem foi R${:.2f} ".format(km*0.45))
    print("Um custo de 45 centavos por KM")
