'''
Escreva um programa que calcule o tempo de viagem de carro.
Pergunte a distância a percorrer e a velocidade média para a viagem

'''

def tempo(distancia,velocidade):
    return (distancia/velocidade)

dist=float(input("Digite a distancia percorrida em kms: "))
vel=float(input("Digite a velocidade percorrida em km/h: "))
print("O tempo de viagem foi {:.2f} horas " .format(tempo(dist,vel)))