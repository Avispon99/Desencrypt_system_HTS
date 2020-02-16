while 1:

	question = input('Encrypt (1)  -  Desencrypt (2) : ')

	if question == '1':

		word=input('Write word to Encrypt: ')
		count=0
		list_add=[]

		"""
		El ciclo de 'range' que representa las posiciones ASCII debe 
		anidarse dentro del ciclo de 'word' que representa la palabra 
		a encriptar, ya que si se anida de forma opuesta podria hallar
		coincidencias de posiciones ASCII en un orden distinto al de
		la lista 'word' por lo que el sistema de encryptado que debende
		mucho del orden de la palabra se romperia.
		"""
		for character in word: 
			for i in range(127): 
				if chr(i) == character:   # 'chr' convierte un numero entero en su caracter ASCII correspondiente.
					print('\nNormal: ',i,character)
					print('Encrypt: ',i+count,chr(i+count),'\n')
					list_add.append(chr(i+count))
					count+=1

		encrypt=''.join(list_add)
		print('Word Encrypt: '+encrypt)


	elif question == '2':

		word=input('Write word to Desencrypt: ')
		count=0
		list_add=[]


		for character in word: 
			for i in range(127): 
				if chr(i) == character:   # 'chr' convierte un numero entero en su caracter ASCII correspondiente.
					print('\nNormal: ',i,character)
					print('Encrypt: ',i-count,chr(i-count),'\n')
					list_add.append(chr(i-count))
					count+=1

		encrypt=''.join(list_add)
		print('Word Encrypt: '+encrypt)	


	else:
		print('Value Incorrect..\n\n')
		opt=input('Press button to continue - Exit(x)\n\n')
		if opt=='x':
			break 




