# Sempre que criar uma instancia o método init será chamado, independente de quantas
# self = referencia a mim, referencia a uma instancia, atribui que aqueles metodos referenciam uma determinada instancia
# O self é o que vai diferenciar cada atributo mesmo sendo dois iguais por ex.
# Self referencia instancia

class Pessoas:
    def __init__(self, nome, idade, cpf):
       # print(f'{nome} | {idade} | {cpf}')
        self.nome = nome
        self.idade = idade


    def logar_sistema(self):
        print(f'esta logando no sistema')



p1 = Pessoas('Renata', 36, '23425435643')       #sempre que chamar o método Pessoas a função do __init__ será chamada e orintará o olá
