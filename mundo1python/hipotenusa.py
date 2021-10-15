import math

co=float(input("Digite o cateto oposto: "))
ca=float(input("Digite o cateto adjacente: "))
hipotenusa=math.hypot(co,ca)
print("A hipotenusa é igual a {:.2f} ".format(hipotenusa))
