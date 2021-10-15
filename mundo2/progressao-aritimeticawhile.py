print("progressao aritmética com while")
primeiro=int(input("Digite o primeiro termo: "))
razao=int(input("Digite a razao: "))
termo=primeiro
cont=1
while cont>=10:
   print("{} ".format(termo))
   termo += razao
   cont += 1
   #print("{} ".format(termo), end=' ')