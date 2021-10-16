class Retangulo:
    'classe para definir o tamanho do retangulo'

    def tamanho(self,largura, altura):
        'variaveis'
        self.x=largura
        self.y=altura

    def perimetro(self):
        'perimetro do regangulo'
        return 2*(self.x+self.y)

    def area(self):
        'area do retangulo'
        return (self.x*self.y)

'''

p=Retangulo()
p.tamanho(5,4)
p.perimetro()
p.area()



'''




