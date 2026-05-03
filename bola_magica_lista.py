import random

mensagens = ['É certo',
    'É decidido que sim',        
    'Sim, definitavemente',
    'Resposta confusa, tente novamente',
    'Pergunte novamente mais tarde',
    'Concentre-se e pergunte novamente',
    'Minha resposta é não',
    'A perspectiva não é muito boa',
    'muito duvidoso']
print('Faça uma pergunta')
input('>')  # A chamada random.randit gera um número aleatório que será utilizado como índice até -1
print(mensagens[random.randint(0, len(mensagens)- 1)]) # len retorna a quantidade da lista
