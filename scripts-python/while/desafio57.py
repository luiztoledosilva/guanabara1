sexo=str(input('Informe seu sexo [Masculino/Feminino] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo=str(input('Dados Invalidos, por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso '.format(sexo))
