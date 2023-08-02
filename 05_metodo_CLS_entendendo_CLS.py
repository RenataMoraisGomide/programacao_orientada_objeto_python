# Lembrando que o cls é o que usamos com o @classmethod e a diferença dele com os métodos estáticos
# O cls é um parâmetro no qual recebe o estado da classe, ou seja, vc tem tudo que pertence aquela classe
# o self não recebe o estado daquela determinada instância? O cls recebe o estado da classe, as informações daquela classe
# e com isso o cls podemos criar e modificar atributos e método da classe.

class Pessoas:
    possui_olho = True
    possui_boca = True
    raca = 'Ser Humano'

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def retorna_nome(self):
        return self.nome
    
    def logar_sistema(self):
        print(f'{self.retorna_nome()} Está logando no sistema')

    @classmethod
    def andar(cls):
        cls.pernas = 2
        return None

#p1 = Pessoas('Renata', 21)
#p2 = Pessoas('Geórgia', 8)

#p1.logar_sistema()
#p1.andar()

Pessoas.andar(10)         #Não precisa do p1 e p2 pois é um método de classe e não de instância

print(Pessoas.possui_boca)
Pessoas.andar()
print(Pessoas.penas)

