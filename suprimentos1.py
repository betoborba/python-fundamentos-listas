suprimentos = ['Lapis', 'grampeador', 'marcatexto', 'fichario']
# retornará dois valores: o índice do item na lista e o próprio item
# A cada iteração do loop, enumerate retorna o valor
for index, item in enumerate(suprimentos):
    print(' O Index ' + str(index) + ' no lista de suprimentos é ' + item)
