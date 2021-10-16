cont=0
soma=0
nome=' '
sexo=' '
maior=0
##menor=0
idade=0
velho=' '
for i in range(1,5):
    nome=str(input("Digite o nome da {}ª pessoa: ".format(i))).upper()
    sexo=str(input("M p masculino ou F/ feminino p/ {}: ".format(nome.upper())))
    idade=int(input("Digite a idade de {} ".format(nome.upper())))
    soma += idade
    if i==1 and sexo in 'Mm':
        maior=idade
        velho=nome
    if sexo in 'Mm' and idade>maior:
        maior=idade
        velho=nome
    if sexo in 'Ff' and idade<20:
        cont +=1
        
print("O numero de mulheres com menos de 20 anos é {} pessoas ".format(cont))   
print("A pessoa do sexo masculino de nome {} com maior idade = {} anos ".format(velho,maior))   
print("A média de idade do grupo é {:.2f} ".format(soma/4))
    
