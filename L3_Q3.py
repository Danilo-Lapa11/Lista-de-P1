n = int(input())

lista1 = list()
lista2 = list()
lista3 = list()

for a in range(n):  
  analise = input("Insira uma string e um inteiro separados por vírgula: ")
  split_lista = analise.split(",")
  # [conteudo, numero do diario]
  conteudo = split_lista[0].strip()
  numero_do_diario = int(split_lista[1].strip())
  
  if numero_do_diario == 1:
    lista1.append(conteudo)
    diario1 = numero_do_diario
  elif numero_do_diario == 2:
    lista2.append(conteudo)
    diario2 = numero_do_diario
  elif numero_do_diario == 3:
    lista3.append(conteudo)
    diario3 = numero_do_diario
  
m = int(input())
for b in range(m):
  conteudo_buscado = str(input())
  if conteudo_buscado in lista1:
    print(f'Informacoes sobre {conteudo_buscado} estao no Diario {diario1}')
    
  elif conteudo_buscado in lista2:
    print(f'Informacoes sobre {conteudo_buscado} estao no Diario {diario2}')
  
  elif conteudo_buscado in lista3:
    print(f'Informacoes sobre {conteudo_buscado} estao no Diario {diario3}')
  else:
    print(f'Nenhum dos diarios possui informacoes sobre {conteudo_buscado}')