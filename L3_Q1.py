lista = []
pergunta = str(input('Situacao: '))
while not(pergunta == 'ja temos nossa lista de suspeitos'):

    pergunta = str(input('Situacao: '))
    
    if pergunta == 'novo suspeito - altissima periculosidade':
        nome_suspeito = str(input('Qual o nome do suspeito? '))
        lista = lista.insert(0, nome_suspeito)

    elif pergunta == 'novo suspeito - pouco perigoso':
        nome_suspeito = str(input('Qual o nome do suspeito? '))
        lista = lista.append(nome_suspeito)

    elif pergunta == 'livre de suspeita, pode remover':
        nome_suspeito = str(input('Qual o nome do suspeito? '))
        lista = lista.remove(nome_suspeito)

    elif pergunta == 'que estranho, esses dois meliantes… troque-os de lugar':
        nome_suspeito_1 = str(input('Qual o nome do suspeito? '))
        nome_suspeito_2 = str(input('Qual o nome do suspeito? '))
        lista = lista.reverse(nome_suspeito_1, nome_suspeito_2)
    elif pergunta == 'essa posicao nao esta de acordo, ele nao e tao perigoso assim':
        nome_suspeito = str(input('Qual o nome do suspeito? '))
        
        lista = lista.reverse   (nome_suspeito)
    elif pergunta == 'como a lista esta ficando?':
        print(lista)


else:
    print('O resultado final ficou assim:')
    print(lista)
    









        