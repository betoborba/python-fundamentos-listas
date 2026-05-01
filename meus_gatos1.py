nome_gatos = [] # Vetor das informações 
while True: # len(nome_gatos) mostra quantos nomes já foram digitados; +1 indica o próximo número da entrada
    print('Entre com o nome dos gatos ' + str(len(nome_gatos) + 1) + ' (Ou aperte "Enter" nada para parar.):')
    nome = input()
    if nome == '' : # Se o nome estiver vazio pare
        break
    nome_gatos = nome_gatos + [nome] # Concatenação da lista
print ('O nome dos gatos são: ')
for nome in nome_gatos: # Percorre a lista nome_gatos e exibe cada nome armazenado 
    print(' ' + nome)