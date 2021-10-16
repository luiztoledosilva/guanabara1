arquivo = open("produtos.txt", "w")

for i in range(3):
    codigo = int(input("Digite o codigo do produto: "))
    nome = input(input("nome do produto: "))
    preco = float(input("Preco do produto R$ "))
    arquivo.write("codigo = {} \n ".format(codigo))
    arquivo.write("Nome = {} \n ".format(nome))
    arquivo.write("Preco = R${} \n ".format(preco))
arquivo.close()
arquivo = open("produtos.txt", "r")
for linha in arquivo.readlines():
    if preco >= 500:
        print(linha)
arquivo.close()
