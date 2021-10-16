from time import sleep
n1=float(input("Digite um numero: "))
n2=float(input("Digite outro numero: "))
op=0
while op !=7:
    print("""As opções são 1 p soma, 2 p subtração, 3 p multiplicação,
             4 p divisao, 5 p maior, 6 p outros numeors,
             7 p sair """)
    op=int(input("Digite a opção: "))
    if op==1:
        soma=n1+n2
        print("Soma de {}+{}={} ".format(n1,n2,soma))
    elif op==2:
        sub=n1-n2
        print("Subtração de {}-{}={} ".format(n1,n2,sub))
    elif op==3:
        mult=n1*n2
        print("Subtração de {} X {}={} ".format(n1,n2,mult))
    elif op==4:
        div=n1/n2
        print("Subtração de {} / {}={} ".format(n1,n2,div))
    elif op==5:
        if n1>n2:
            maior=n1
        elif n2>n1:
            maior=n2
        else:
            print("numeros iguais!")
        print(" maior numero entre {} e {} é o {} ".format(n1,n2,maior))
    elif op==6:
        print("Informe outros numeros: ")
        n1=float(input("Digite um numero: "))
        n2=float(input("Digite outro numero: "))
    elif op==7:
        print("Saiu!")
    else:
        print("opcao invalida!")
    ##sleep(2)
    
    




