#!/usr/bin/env python3

import csv

with open('padron.txt','r') as padron:
	archivo = padron.readlines()

with open('padron_definitivo_2019.csv','w') as padron_csv:
	padron_escritor = csv.writer(padron_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	padron_escritor.writerow(['NRO DNI', 'TIPO DNI', 'CLASE', 'APELLIDO', 'NOMBRES', 'DOMICILIO', 'CIRCUITO', 'MESA', 'ORDEN'])
	lista = iter(archivo)
	while True:
		try:
			linea = next(lista)
		except StopIteration:
			break
		if linea[0:9] == 'CIRCUITO:':
			circuito = linea[10:(linea.find("-") - 1)]
			continue 

		elif linea[0:5] == 'MESA:':
			mesa = linea[6:-1]
			continue

		elif linea[0:10] == 'NRO. ORDEN':
			#flag = True
			renglon = list()
			linea = next(lista)
			renglon.append(linea) #agrego el numero de orden al renglon
			while True:
				linea = next(lista)
				renglon.append(linea)
				if linea[-5:-1] == 'VOTÓ':
					break
			print(renglon)
			lista_aux= renglon[-1][0:-1].split(' ')
			print(lista_aux)
			tipo_dni = lista_aux[2]
			nro_dni = lista_aux[1]
			clase = lista_aux[3]
			domicilio = renglon[-2][0:-1]
			orden = renglon[0][0:-1]
			if len(renglon) == 4:
				lista_aux = renglon[1].split(',')
				apellido = lista_aux[0]
				nombres = lista_aux[1][0:-1]
			else:
				lista_aux = renglon[1].split(',')
				apellido = lista_aux[0]
				nombres = lista_aux[1][0:-1] + renglon[2][0:-1]
			padron_escritor.writerow([nro_dni,tipo_dni,clase,apellido,nombres,domicilio,circuito,mesa,orden])
		else:
			continue



		"""if linea[0:10] == 'NRO. ORDEN':
			flag = True
			linea = next(lista)
			orden = linea[0:-1]
			linea = next(lista)
			lista_aux = linea.split(',')
			apellido = lista_aux[0]
			nombres = linea[1][1:-1]
			linea = next(lista)
			domicilio = linea[0:-1]
			linea = next(lista)
			lista_aux = linea.split(' ')
			print(lista_aux)
			nro_dni =  lista_aux[1]
			tipo_dni = lista_aux[2]
			clase = lista_aux[3]
		else:
			flag = False

		if flag:
			padron_escritor.writerow([nro_dni,tipo_dni,clase,apellido,nombres,domicilio,circuito,mesa,orden])"""





