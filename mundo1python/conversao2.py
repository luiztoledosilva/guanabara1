D='\033[;0m'
VM='\033[1;31m'
M='\033[1;30m'




print(f"""

{VM}  卐卐            卐卐卐卐卐卐卐卐
卐  卐          卐                卐
{D}卐  卐          卐  卐卐卐卐卐卐卐卐
卐  卐          卐  卐
{M}卐  卐          卐  卐
卐  卐          卐  卐
{VM}卐  卐          卐  卐
卐  卐卐卐卐卐卐卐  卐卐卐卐卐卐卐
{D}卐<========EDIT-D404RBLACK=======>卐
  卐卐卐卐卐卐卐卐  卐卐卐卐卐卐  卐
            {M}    卐  卐        卐  卐
                卐  卐        卐  卐
              {VM}  卐  卐        卐  卐
                卐  卐        卐  卐
  {D} 卐卐卐卐卐卐卐   卐        卐  卐
 卐                 卐        卐  卐
{M} 卐卐卐卐卐卐卐卐卐卐         卐卐
{D}
""")




num=int(input("Digite um numero pra conversao: "))
print (" ")
V='\033[1;32m' #em uso
D='\033[;0m' #em uso
VM='\033[1;31m' # em uso
B='\033[1;34m' # em uso
C='\033[1;37m'
CY='\033[1;36m'
A='\033[1;33m'
R='\033[1;35m' # em uso
MG='\033[1;95m'
M='\033[1;35m'

while True:
    print(f"""Escolha um numero pra conversao:
 {V}[1] Para binario
 {D}[2] Para Octal
 {B}[3] Para hexadecimal
 {R}[00] para sair do programa
 """)
    print ("="*20)
    opcao=int(input(f"{VM}Digite a opcao: "))
    if opcao==1:
            binario=bin(num)
            print(f"O numero {num} corresponde em binario em {binario} ")
    elif opcao==2:
            octal=oct(num)
            print(f"O numero {num} corresponde em decimal em {octal} ")
    elif opcao==3:
            hexadecimal=hex(num)
            print(f"O numero {num} corresponde em hexadecimal em {hexadecimal} ")
    elif opcao == 00:
        print (f"{A}☆Saindo do programa☆")
        break