# NÃO CONFUNDIR COM MÉTODO DE CLASSE (NÃO SÃO A MESMA COISA)
# 
# Método de classe é um método na qual ele pode ser chamado sem precisar de uma instância apenas pela classe.
# sempre que usamos o @classmethod ele precisa receber o (cls) que é o estado  da sua classe. Ele representa sua classe em si
# e atraves do cls você pode ver, modificar, apagar, usar os elementos que estiverem dentro do (cls)

# Método estático é um método que pode ser chamado sem precisar da instância apenas pela classe mais ele é um método utilitário
# ele não consegue acessar nem modificar nenhum atributo ou método de classe.


#  @estaticmethod

#ex:

@staticmethod

def e_adulto(idade):
    if idade > 18:
        return True
    return False

print(Pessoas.e_adulto(20))   #True