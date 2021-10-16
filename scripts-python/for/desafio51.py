"""
 progressao aritimetica
"""
print("Progressao Aritimética!")
primeiro=int(input("Primeiro termo: "))
razao=int(input("Razao: "))
decimo=primeiro+(10-1)*razao
for termos in range(primeiro,decimo+razao,razao):
    print(termos, end=' ')
print("Fim")
