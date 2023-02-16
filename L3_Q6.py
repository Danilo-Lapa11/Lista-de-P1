analises = int(input())
for a in range(analises):
	# estrutura de msg_codificada: 00 x-y
	# 00 é o ultimo termo desejado da sequencia de fibonacci 
	# x-y sáo os indices da sub lista que vão ser concatenados 

	msg_codificada = input()
	# a entrada vai ser dividida em termos por meio do split separada por espaco
	split_msg_codificada = msg_codificada.split( )
	# split_msg_codificada = [ termo_fib , cordenada ]
	termo_fib = int(split_msg_codificada[0].strip())
	coordenada = split_msg_codificada[1].strip()

    # Agora iremos repitir o processo de split na string coordenada para dividir a string quando ver o '-'
	valores_xy = coordenada.split('-')

	# Sequencia de fibonacci usando termo_fib como limite pro while
	# 1 , 1 , 2 , 3 , 5 ...
	# t1, t2 , t3, ...
	t1 = 1
	t2 = 1
	cont = 3
	
	while (cont <= termo_fib) :
		t3 = t2 + t1
		t1 = t2
		t2 = t3
		# essa relacao t1 = t2 e t2 = t3, faz com que os termos permutem a cada repetição do while
		# 1 ,  1 ,  2 ,  3 ,  5  ...  
		# t1 + t2 = t3 ,         ...  
		#      t1 + t2 = t3      ...
		#           t1 + t2 = t3 ...
		cont += 1

	# Convertendo t3 (resultado de fibonacci) para string podemos iterar a string adicionando cada algarismo em uma lista
	t3_str = str(t3)
	t3_algarismos = []
	for x in t3_str:
		t3_algarismos.append(x)
	# t3_algarismos = [ 0, 1, 2, 3, 4 ...] com seus index assim

	x = int(valores_xy[0])
	y = int(valores_xy[1])

	# Agora iremos usar os valores de x e y para extrair os algarismos do termo de fibonacci e concatenar eles
	index_x = t3_algarismos[x] # numero em string
	index_y = t3_algarismos[y] # numero em string

	xy = index_x + index_y 
	codg_ASCII = int(xy)
	# Agora damos print no valor de codg_ASCII usando a função chr() para transformar o codigo em letra
	print(chr(codg_ASCII), end='')

	# por fim temos que dar clear() na listas ao final do loop para que sejam armazenados outros valores
	split_msg_codificada.clear()
	t3_algarismos.clear()
    