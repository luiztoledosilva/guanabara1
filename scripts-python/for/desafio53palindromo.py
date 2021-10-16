frase=str(input("Digite uma frase: ")).strip().upper() ###desconsiderar espaco vazio
palavra=frase.split() #pedaço              ##letra maiuscula 
junto=' '.join(palavra)  #juntar frase inteira
inverso=' ' ##variavel que vai receber o inverso da letra
for letra in range(len(junto)-1,-1,-1): #len = tamanho da letra
    inverso += junto[letra] #frase invertida
if inverso == junto:
    print("Temos um palindromo")
else:
    print("Nao temos um palindromo")

print(junto, inverso)
