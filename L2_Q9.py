# recebe um valor em binario e converte pra decimal para verificar se o valor corresponde aos casos emq ue ganha uma viagem.

# Algoritmo conversor de binario pra decimal
n_binario = int(input())
n = len(str(n_binario))
valor_digitado = n_binario
decimal = 0
i = 0

while n >= 0 :
  resto = n_binario % 10
  decimal = decimal + (resto * (2**i))
  n = n - 1
  i = i + 1
  n_binario = n_binario // 10

chances = 3
for x in range (0,chances):
  palpite = int(input())
  if (palpite == decimal) and (decimal == 1) :
    print('Parabéns!! Você acertou!')
    print('Férias inesquecíveis estão te esperando!')
    print('Seu destino será Porto de Galinhas (BRA).')
    print('Prepare-se para viver dias incríveis desfrutando das riquezas naturais da nossa região!')
    break
  elif (palpite == decimal) and (decimal == 2):
    print('Parabéns!! Você acertou!')
    print('Férias inesquecíveis estão te esperando!')
    print('Seu destino será Fernando de Noronha (BRA).')
    print('Belíssimas praias estão por vir.')
    print('Não esqueça o protetor solar.')
    break
  elif (palpite == decimal) and (decimal == 3):
    print('Parabéns!! Você acertou!')
    print('Férias inesquecíveis estão te esperando!')
    print('Seu destino será Gramado (BRA).')
    print('Aproveite passeios e paisagens espetaculares no sul do país!')
    break
  elif (palpite == decimal) and (decimal == 4):
    print('Parabéns!! Você acertou!')
    print('Férias inesquecíveis estão te esperando!')
    print('Seu destino será Berlim (ALE).')
    print('Desfrute de muita cultura e de experiências incríveis!')
    print('Prepare os casacos de frio!')
    break
  elif (palpite == decimal) and (decimal == 5):
    print('Parabéns!! Você acertou!')
    print('Férias inesquecíveis estão te esperando!')
    print('Seu destino será Tóquio (JPN).')
    print('Viva uma experiência inesquecível explorando um país do outro lado do mundo.')
    print('Prepare-se para muitas horas de voo!')
    break
  elif (palpite == decimal) and (decimal > 5):
    print('Parabéns!! Você acertou!')
    print('Mas, infelizmente, hoje não é o seu dia de sorte.')
    print('Apesar de ter dado a resposta correta, seu bilhete não oferece nenhum prêmio.')
    print('Sinta-se à vontade para conhecer nossos pacotes e outras promoções imperdíveis com um de nossos vendedores!')
    break    
  elif (palpite != decimal) and (chances > 1):
    chances -= 1
    print(f'Resposta incorreta. Mas não desista! Você ainda tem {chances} chance(s).')
  elif (palpite != decimal) and (x == 2):
    chances -= 1
    if 5 >= decimal >= 1 :
      print('Infelizmente mais uma resposta incorreta.')
      print('Agradecemos sua participação!')
      print('Seu bilhete era premiado. Que pena!')
    else:
      print('Infelizmente mais uma resposta incorreta.')
      print('Agradecemos sua participação!')
      print('Pelo menos seu bilhete não era premiado.')
      print('Sinta-se à vontade para conhecer nossos pacotes e outras promoções imperdíveis com um de nossos vendedores!')