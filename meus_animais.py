meus_animais = ['Merlin', 'Lineu', 'Coraline']  # Lista declarada
print('Entre com o nome do animal: ')
nome = input()  # Entrada do nome
if nome not in meus_animais:  # Se a entrada não tiver na minha lista
    # frase + nome gitado
    print('Eu não tenho esse um animal com esse nome ' + nome)
else:
    print(nome + ' É o meu gato')  # Se não entrada é o gato

# O programa necessita de um ajuste para o tratamento da entrada pois não é diferenciado maiúscula e minúscula
