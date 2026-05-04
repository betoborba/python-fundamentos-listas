def cozinha(item_parametro):
    item_parametro.append('geladeira')


panela = [1, 2, 3]
cozinha(panela)
print(panela)  # Exibe na tela [1, 2, 3, 'geladeira']
