from random import shuffle


class Baralho:

    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __repr__(self):
        return "Carta('{}', '{}')".format(self.valor, self.naipe)

    def __eq__(self, outro):
        return self.valor == outro.valor and self.naipe == outro.naipe
p=Baralho().randint
#p.valor()
#p.naipe()
