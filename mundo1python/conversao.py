num=int(input("Digite um numero pra conversao: "))
print(""" Escolha um numero pra conversao:
[1] Para binario
[2] Para Octal
[3] Para hexadecimal

""")
opcao=int(input("Digite a opcao: "))
if opcao==1:
    binario=bin(num)
    print(f"O numero {num} corresponde em binario em {binario} ")
elif opcao==2:
    octal=oct(num)
    print(f"O numero {num} corresponde em decimal em {octal} ")
elif opcao==3:
    hexadecimal=hex(num)
    print(f"O numero {num} corresponde em hexadecimal em {hexadecimal} ")