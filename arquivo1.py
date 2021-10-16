'''

Faça um programa para criar um arquivo chamado "aluno.txt", que deverá armazenar os seguintes dados:
nome, RA, curso, informados pelo usuário

nome=input("Digite o nome do aluno: ")
arquivo=open("aluno.txt",'a')
arquivo.write(nome)
ra=input('Digite o RA do aluno: ')
arquivo=open("aluno.txt",'a')
arquivo.write(ra)
curso=input("Digite o curso do aluno: ")
arquivo=open("aluno.txt",'a')
arquivo.write(curso)
arquivo.write
'''
arquivo=open("aluno.txt",'a')
nome=input("Digite o nome do aluno: ")
ra=input('Digite o RA do aluno: ')
curso=input("Digite o curso do aluno: ")
##arquivo.write("O aluno {} com RA {} esta matriculado no curso {} \n" .format(nome,ra,curso))
#arquivo.write("Alunos \n")
arquivo.write("nome = {} \n".format(nome))
arquivo.write("RA = {} \n".format(ra))
arquivo.write("Curso = {} \n".format(curso))


print("O aluno {} com RA {} esta matriculado no curso {} " .format(nome,ra,curso))
arquivo.close()

arquivo = open("aluno.txt", "r")
for linha in arquivo.readlines():
    print(linha)
arquivo.close()
'''
Faça um programa para recuperar e imprimir na tela o conteúdo do arquivo "aluno.txt".


'''