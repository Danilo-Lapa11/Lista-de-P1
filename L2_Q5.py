# Votação para melhor lugar pra ir.
# O melhor lugar será aquele que possuir o maior total de pontos, enquanto o pior lugar, o que possuir o menor total.

N = int(input())

maior_nota = 0
menor_nota = 0
melhor_lugar = str()
pior_lugar = str()
empate = False

for i in range(0, N):
  nome_lugar = str(input(''))
  soma = 0
  
  for x in range(1, 10):
    nota = int(input())

    if nota >= 0:
      soma += nota
    else:
      break

  if i == 0:
    menor_nota = soma
    maior_nota = soma
    melhor_lugar = nome_lugar
    pior_lugar = nome_lugar
    
  else:
    # Quando a soma obtida na chamada do for é maior ou menor que a do for == 0 (primeira chamada)
    
    if soma > maior_nota:
      maior_nota = soma
      melhor_lugar = nome_lugar
      empate = False
      
    elif (soma < menor_nota):
      menor_nota = soma
      pior_lugar = nome_lugar
      empate = False
      
    # Caso haja empate das somas das notas com a melhor nota o nome do lugar é concatenado na variavel de melhor_lugar
      
    elif (maior_nota == soma) :
      melhor_lugar += f', {nome_lugar}'
      empate = True

if (empate == True):
  print(melhor_lugar)
  print('Tantas opções')
else:
  print('{} ganhou de lavada de {}, com {} vs {}'.format(melhor_lugar, pior_lugar, maior_nota, menor_nota))
  
