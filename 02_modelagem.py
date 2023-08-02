#Continuação do 01_POO.py
# Para modelagem, o primeiro passo é analisar quais as informações iremos precisar para o programa, nome, valor, idade, etc...abs
# Para abrir(inicializar) uma modelagem chamamos a classe class que é uma palavra reservada que diz que todas as entidades 
# daquele objeto irá ter.
# De acordo com a convenção python a pep 8 diz que quando dar nome as classe tem que ser letra MAIÚSCULA, tanto se for
# apenas um nome quanto dois ex PessoasClientes:

# Aqui definimos a classe pessoas (que pode ser várias pessoas) que chama instância
class Pessoas:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
    def logar_sistema(self):                                 #Métodos:
        print(f '{self.nome}Estou logando no sistema')       #Função que pertence esclusivamente aquela entidade. Função Python que está dentro da classe
                                                             #Cada atributo agora terá essa chama tb, poderá logar no sistema
                                                             # Usando a função quando chamar logar no sistema virá o nome
        


#Atributos
#aqui vemos a instanca da classe:
p1 = Pessoas('Renata Morais', 21, '23456567889')        #Aqui colocamos a instancia p1 na memória
p2 = Pessoas('Georgia Gomide', 8, '44343434343')        #criando outra instancia com obj diferente pois temos endereços de memória diferente

print(p1.nome)
print(p2.idade)

p1.logar_sistema()    # a pessoa 1 estará logando no sistema.

