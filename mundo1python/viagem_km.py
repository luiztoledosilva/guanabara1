km=float(input("Quantos kms foi a viagem: "))
if km<=200:
    conta=km*0.5
    ##print("A viagem teve o custo de R${:.2f} " .format(conta))
    print(f"A viage teve o custo de {conta:.2f}")
else:
    conta=km*0.45
    ##print("A viagem teve o custo de R${:.2f} ".format(conta))
    print(f"A viage teve o custo de {conta:.2f}")