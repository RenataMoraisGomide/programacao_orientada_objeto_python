# O atributo de classe pode ser acessado pela própria classe. 
# O atributo de classe sempre será o mesmo para todos as 'pessoas' tipo: cabeça toda pessoa tem.
# O atributo de instância é quando temos o self
# Agora quando temos o atributo de classe, significa que nós não precisamos da instância daquela classe
# para acessar aquela variável. 
# o que caracteriza o método de classe é o decorador( @ ) esse @classmethod esse metodo pertence a classe e não a instância
# e dentro dos ( ) usamos o (cls)
#ex:

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
    def andar(cls, velocidade):
        print('Estou andando na velocidade {velocidade} m/s')

#p1 = Pessoas('Renata', 21)
#p2 = Pessoas('Geórgia', 8)

#p1.logar_sistema()
#p1.andar()

Pessoas.andar(10)         #Não precisa do p1 e p2 pois é um método de classe e não de instância


