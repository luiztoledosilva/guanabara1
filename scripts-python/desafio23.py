print("Desafio 23")
n=int(input("Digite um numero com 4 digitos: "))
u=n//1%10
d=n//10%10
c=n//100%10
m=n//1000%10
print("Unidade: {} ".format(u))
print("Dezena: {} ".format(d))
print("Centena: {} ".format(c))
print("Milhar: {} ".format(m))
