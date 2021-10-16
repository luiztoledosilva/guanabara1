class funcionario:
    def __init__(self,nome , data_admissao, salario):
        self.nome=nome
        self.data_admissao= data_admissao
        self.salario=salario

    def set_nome(self, nome):
        self.nome = nome

    def set_data_admissao(self, data_admisao):
        self.data_admissao = data_admissao

    def set_salario(self,salario):
        self.salario = salario

    def get_informs(self):
        return self.nome, self.data_admissao, self.salario

class gerente(funcionario):

    def __init__(self, nome, data_admissao, salario):
        super(gerente, self).__init__(nome, data_admissao, salario)
        self.bonus = self.salario * 0.4

    def get_informs(self):
        return self.nome, self.data_admissao, self.salario,self.bonus

func_gerente=gerente("LUiz","01/10/2017",8000)
nome, admissao, salario, bonus = func_gerente.get_informs()

print(f"Nome: {nome} \n Data de admissão: {admissao} \n Salário: R$ {salario} \n Bonus: R$ {bonus}")

