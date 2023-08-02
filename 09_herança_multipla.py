# A herança multipla tem que ser usada com sabedoria, as vezes pode gerar erros quando temos repetidas heranças


#CALSSE PAI:
class Animal:
    def andar(self):
        print('Estou andando')
    
    def correr(self):
        print('Estou correndo')
    
    def pular(self):
        print('Estou pulando')

class Felino(Animal):
    def felino(self):
        print('Eu sou um felino')


class Gato(Felino):             #Aqui teremos a herança multipla, onde o gato herda de animal e de felino
    def miar(self):
        print('Estou miando como gato')


class Cachorro(Animal):
    def latir(self):
        print('Estou latindo')


y = Gato()
y.miar()
y.pular()
y.correr()

print('--------####---------')

x = Cachorro()
x.latir()
x.correr()
x.pular()


