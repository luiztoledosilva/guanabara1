"""
aula de string - python

"""
frase='Curso em Video Python'
print(frase)  ##mostrar frase inteira
print(frase[3])    ##mostrar a partir da letra 3, comecando do zero
print(frase[3:13]) ##mostrar a partir da letra 3 até 13, excluindo o 13
print(frase[:13]) ## do inicio ao 13, excluindo o 13
print(frase[1:15]) ###eliminou se a primeira letra, pois se começa com 0
print(frase[1:15:2]) ### :2 pular de 2 em 2 
print(frase[::2]) #pulando de 2 em 2
print( """

- Eu amo o mundo! Eu detesto o mundo! Eu creio em Deus!
Deus é um absurdo! Eu vou me matar! Eu quero viver!
- Você é louco?
- Não, sou poeta.


"""
### acima pode ser usado para menu no python, por exemplo
)
print(frase.count('o')) ##contar qts letras o tem na frase
print(frase.count('O')) ##o python diferencia maiusculo de minisculo
print(frase.upper().count('O')) ##upper colocar frase em maiuscula e lower em minuscula
print(len(frase)) #ver o comprimento da frase
print(len(frase.strip())) #ver o comprimento da frase sem o espaço em branco
print(frase.replace('Python','Android')) #substituicao de palavras
print(frase.find('Curso')) ##encontrar posicao
print(frase.find('video')) #-1
print(frase.lower().find('video'))
print(frase.split())  #dividida
dividido=frase.split()
print(dividido[0])
print(dividido[2][3])




