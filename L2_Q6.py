#contadores de Falhas, Etapas realizadas e Despesa Total ---- Pré sets
total_falhas = 0
etapas_REALIZADAS = 0 
despesa_total = 0
loop = True

nome_invencao = str(input(''))

while (loop == True):
  nome_etapa = str(input(''))
  
  # Etapa Geral - Validacao do status da etapa 
  if (nome_etapa != 'dar um plus') and (nome_etapa != 'desistir') and (nome_etapa != 'concluir'):
    custo_etapa = int(input())
    tentativas = int(input())
    
    for x in range(0, tentativas):
      status_etapa = str(input(''))
      
      # Status Incorreto
      if status_etapa == 'incorreto' :
        despesa_total += custo_etapa
        total_falhas += 1
        print(f'Ainda não consegui {nome_etapa} corretamente, e essa tentativa me custou R${custo_etapa}') 
      # Status Correto
      elif(status_etapa == 'correto'):
        despesa_total += custo_etapa
        etapas_REALIZADAS += 1
        print(f'Oba! consegui {nome_etapa}, o que me custou R${custo_etapa}')
        break
    #Etapa Andamento do projeto depois do STATUS
    print (f'ANDAMENTO DO PROJETO: Etapas realizadas - {etapas_REALIZADAS} ; Tentativas falhas - {total_falhas}')
           
  # Etapa Dar um Plus
  if (nome_etapa == 'dar um plus'):
    custo_etapa = int(input())
    print(f'Agora o(a) {nome_invencao} ficou ainda mais legal! Pena que precisei gastar R${custo_etapa}')
    despesa_total += custo_etapa
    
  # Etapa Desisistir ou Concluir 
  if (nome_etapa == 'desistir'):
    print(f'A jornada da construção do(a) {nome_invencao} acaba aqui.')
    print(f'Infelizmente, o sonho do(a) {nome_invencao} foi interrompido e levou junto com ele R${despesa_total}')
    loop = False   
  elif (nome_etapa == 'concluir'):
    print(f'A jornada da construção do(a) {nome_invencao} acaba aqui.')
    print(f'Uhuuu, finalmente o(a) {nome_invencao} tá pronto(a)! Esse projeto me custou R${despesa_total}')
    loop = False  
