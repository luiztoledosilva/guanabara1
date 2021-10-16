"""
 progressao aritimetica regressiva
"""
print("Progressao Aritimética!")
primeiro=int(input("Primeiro termo: "))
razao=int(input("Razao: "))
decimo=primeiro+(10-1)*razao
for termos in range(decimo,primeiro-razao,-razao):
    print(termos, end=' ')
print("Fim")
