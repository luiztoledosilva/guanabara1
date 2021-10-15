maior=0
menor=0
for p in range(1,6):
    peso=float(input("Digite o peso da %d da pessoa: " %p))
    if p==1:
        maior=peso
        menor=peso
    else:
        if peso>maior:
            maior=peso
        if peso<menor:
            menor=peso
print("maior peso = {:.2f}" .format(maior))
print("menor peso = {:.2f}" .format(menor))