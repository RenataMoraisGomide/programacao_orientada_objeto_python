# Imaginemos que tenhamos um e-commerce e nesse caso teriamos um vendedor e um cliente.

#sem utilizarmos a herança teriamos que correr um código muito longo e repetitivo assim:
class Vendedor:
    def falar(self):
        print('Estou falando')
    def andar(self):
        print('Estou andando')
    def vender(self):
        print('Estou vendendo')
class Cliente:
    def falar(self):
        print('Estou falando')
    def andar(self):
        print('Estou andando')
    def comprar(self):
        print('Estou comprando')

#ENTÃO USAMOS A HERANÇA PARA MELHORAR ESSE CÓDIGO USANDO A HERANÇA, FICANDO ASSIM:

class Pessoa:                        # Ambos (cliente e vendedor)
    def andar(self):
        print('Estou andando')
    def falar(self):
        print('Estou falando')

class Cliente(Pessoa):              # Aqui significa que estamos criando uma nova classe/entidade Cliente que faz tudo que a classe Pessoa faz
    def comprar(self):
        print('Estou comprando')

class Vendedor(Pessoa):
    def vender(self):
        print('Estou vendendo')



c1 = Cliente()


c1.andar()
c1.falar()
c1.comprar()

v1 = Vendedor()

v1.andar()
v1.falar()
v1.vender()






