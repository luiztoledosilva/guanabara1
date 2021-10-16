print("Numero decimal para outra base ")
num=int(input("Digite um numero inteiro: "))
print("""Esolha uma das bases para conversão:
[1] Binario
[2] Octal
[3] Hexadecimal """)
opcao=int(input("Qual a sua opção? "))
if opcao==1:
    print("O numero decimal {} em binario = {} ".format(num, bin(num)[2:]))
elif opcao==2:
    print("O numero decimal {} em octal = {} ".format(num, oct(num)[2:]))
elif opcao==3:
    print("O numero decimal {} hexamadecimal = {} ".format(num, hex(num)[2:]))
else:
    print("Opção inválida!")
