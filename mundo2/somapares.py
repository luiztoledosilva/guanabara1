soma=0
cont=0
for i in range(1,7):
    num=int(input("Digite o numero %d° numero " %i))
    if num%2==0:
        cont=cont+1
        soma=soma+i
print(f"a soma {cont} dos numeros pares = {soma} ")

##Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.