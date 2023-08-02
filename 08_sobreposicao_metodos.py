# Primeira coisa que temos que entender é que para que haja uma sobreposição de métodos é preciso que haja uma Herança


class Pessoa:                       
    def andar(self):
        print('Estou andando')
    def falar(self):
        print('Estou falando')

class Cliente(Pessoa):              
    def comprar(self):
        print('Estou comprando')

    def falar(self):   
        super().falar()                                    #Quando usamos o falar (que já é um método de Pessoa) sobrepusemos ele com um novo print('Estou gritando)
        print('Estou gritando')             #Portanto quando chamamos ele em c1 ele estará gritando e não falando

                                            # Se quisermos referênciar a classe pai usamos o super


c1 = Cliente()

c1.comprar()
c1.falar()