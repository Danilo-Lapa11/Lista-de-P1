#INPUTS

#Derrotei um alien com o diamente
# O XLR8 levou mais um
# Fantasmático botou mais um pra correr
# Por hoje já deu

cont_aliens = -1

for i in range(0,10):
  entrada = input('')
  cont_aliens += 1
  if (entrada == 'O relógio descarregou!') :
    print('Corra Ben! Você já derrotou {} aliens'.format(cont_aliens))
    break
  
  elif (entrada == 'Por hoje já deu'):
    print('Muito Ben Ben! hehe você derrotou {} aliens hoje'.format(cont_aliens))
    break

# OUTPUT

# Muito Ben Ben! hehe você derrotou 3 aliens hoje