arquivo=open("media.txt", "w")
n1=float(input("Digite a nota 1: "))
n2=float(input("Digite a nota 2: "))
media=(n1+n2)/2
arquivo.write("media de {} + {} = {:.2f} \n " .format(n1,n2,media))

arquivo = open("media.txt", "r")
for linha in arquivo.readlines():
    print(linha)
arquivo.close()

