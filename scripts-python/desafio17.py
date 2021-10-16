import math
adj=float(input("Digite o cateto adjacente: "))
opo=float(input("Digite o cateto oposto: "))
hip=pow(adj,2)+pow(opo,2)
hip2=math.sqrt(hip)
print("O valor da hipotenusa eh {} ".format(hip2)) 
