# notes para analise do codigo:
# p = posição da lista
# v = valor da lista

lista = []
loop = True
while (loop == True):
  status_suspeito = str(input(''))
  #ok 
  if (status_suspeito == "novo suspeito - altissima periculosidade"):
    nome_suspeito = str(input())
    lista.insert(0, nome_suspeito)
  #ok
  elif(status_suspeito == "novo suspeito - pouco perigoso"):
    nome_suspeito = str(input())
    lista.append(nome_suspeito)
  #ok
  elif(status_suspeito == "livre de suspeita, pode remover"):
    nome_suspeito = str(input())
    lista.remove(nome_suspeito)
    
  elif(status_suspeito == "sujeito mais perigoso do que pensavamos"):
    pos_old = int(input())
    pos_new = int(input())
    temp = lista[pos_old]
    lista[pos_old] = lista[pos_new]
    lista[pos_new] = temp

  #ok
  elif(status_suspeito == "que estranho, esses dois meliantes… troque-os de lugar"):
    nome_1 = input("")
    nome_2 = input("")
    indice_1 = lista.index(nome_1)
    indice_2 = lista.index(nome_2)
    lista[indice_1], lista[indice_2] = lista[indice_2], lista[indice_1]
  #ok
  elif(status_suspeito == "essa posicao nao esta de acordo, ele nao e tao perigoso assim"):
    nome_lista = str(input(''))
    if nome_lista in lista:
      lista.remove(nome_lista)
      lista.append(nome_lista)
  #ok
  elif(status_suspeito == "como a lista esta ficando?"):
    print(*lista)
  #ok
  elif(status_suspeito == "ja temos nossa lista de suspeitos"):
    loop = False
else: 
    #ok
    print('O resultado final ficou assim:')
    print(*lista)
