"""
Tabela 1: Contribuição INSS
Salário de contribuição (R$)	Alíquota INSS
include                         7,5%
de 1.045,01 até 2.089,60	9%
de 2.089,61 até 3.134,40	12 %
de 3.134,41 até 6.101,06	14%
 

Tabela 2: Alíquotas do Imposto de Renda
Base de cálculo (R$)	Alíquota (%)	Parcela a deduzir do IR (R$)
de 1.903,99 até 2.826,65	7,5%	142,80
de 2.826,66 até 3.751,05	15%	354,80
de 3.751,06 até 4.664,68	22,5%	636,13
acima de 4.664,68	        27,5%	869,36

"""

print("Imposto de renda")
salario=float(input("Digite o valor do salario R$ "))
dependentes=int(input("Digite o numero de dependentes: "))
##deducao=151
if salario<1045.01:
    inss=salario*0.075
    print("O inss a ser pago eh = R$%.2f " %inss)
if salario>=1045.01 and salario<2089.61:
    inss=salario*0.09
    print("O inss a ser pago eh = R$%.2f " %inss)
if salario>=2089.61 and salario<3134.41:
    inss=salario*0.12
    print("O inss a ser pago eh = R$%.2f " %inss)
if salario>=3134.41 and salario<6101.06:
    inss=salario*0.14
    print("O inss a ser pago eh = R$%.2f " %inss)
if salario>=6101.06:
    inss=840
    print("O inss a ser pago eh = R$%.2f " %inss)
#print("O inss a ser pago eh = R$%.2f " %inss)
deducao=(151*dependentes)+inss
base=salario-deducao
if base<1903.99:
    print("Isento de imposto")
else:
    if base>=1903.99 and base<2826.66:
        irrf=base*0.075
        retido=irrf-142.80
        print("O imposto de renda foi de R$%.2f " %irrf)
        print("O imposto retido foi de R$%.2f " %retido)
    elif base>=2826.66 and base<3751.06:
        irrf=base*0.15
        retido=irrf-354.80
        print("O imposto de renda foi de R$%.2f " %irrf)
        print("O imposto retido foi de R$%.2f " %retido)
    elif base>=3751.06 and base<4664.68:
        irrf=base*0.225
        retido=irrf-636.13
        print("O imposto de renda foi de R$%.2f " %irrf)
        print("O imposto retido foi de R$%.2f " %retido)
    else:
        irrf=base*0.275
        retido=irrf-869.36
        print("O imposto de renda foi de R$%.2f " %irrf)
        print("O imposto retido foi de R$%.2f " %retido)




                    
                    
