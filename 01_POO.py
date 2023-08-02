# Paradigma de programação é uma forma de estruturar um raciocínio para chegar a um objetivo.
# Objeto é a modelagem de uma entidade, (dados) que pode ser várias pessoas (dados)
# As 'caracteírsticas' seriam os atributos e os 'métodos' são o que as 'pessoas' fazem, as ações que elas fazem.
# 
# 
# 1= Usando a programação comum, montariamos uma lista de números pares assim:
# Primeiro cria um laço de repetição, que passa por cada valor, depois verifica se cada um valor é par e depois adiciona
# dentro de x
x = []
for i in range(0, 10):
    if i % 2 == 0:
        x.append(i)

# 2= A mesma forma acima usando list comprehension:
x = [i for i in range(0, 10) if i % 2 == 0]



