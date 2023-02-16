Ptt_solar = False
carteira = 0
clima = str('ensolarado')
clima_0 = "ensolarado"
clima_1 = "chuvoso"

# Faz as perguntas e a manipulação de dados das variaveis acima 

for x in range(0,10):
  ask = input('')

  if (ask == 'passar protetor'):
    Ptt_solar = True
  elif (ask == 'choveu'):
    clima = clima_1
  elif (ask == 'parou de chover'):
    clima = clima_0
  elif (ask == 'separar dinheiro'):
    dinheiro = float(input(''))
    carteira = carteira + dinheiro
  elif (ask == 'ir para a praia'):   # Uso do break pra quebrar o for e não dar erro de EOF
    break
  
# printa primeira saida

if (clima == clima_1):
  print('Hoje não vai dar pra ir, chuvinha barrou')
elif (clima == clima_0):
  print('Hoje tem sol e mar!')
  
  # printa segunda saida
  
  if (Ptt_solar == False) and (carteira < 10):
    print('Você não chegou muito bem, chame um médico!')
  elif (Ptt_solar == False) and (carteira >= 10):
    print('O novo camarão do CIn foi criado')
  elif (Ptt_solar == True) and (carteira < 10):
    print('Só faltou uma aguinha de coco...')
  elif (Ptt_solar == True) and (carteira >= 10):
    print('Aí sim! Hoje rendeu!')

