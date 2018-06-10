import csv
import random
import argparse

def main():

	parser = argparse.ArgumentParser(description='crucigramaTP2')
	parser.add_argument('-s', '--solucion', action='store_true', help='imprimir la solucion')
	args = parser.parse_args()

	imprimir_solucion = args.solucion # es True si el usuario incluyó la opción -s

	dic = manejo_archivo('palabras.csv')
	pal_hor,posiciones = horizontal(dic)
	pal_ver = verticales(pal_hor, dic, posiciones)
	imp_matriz(pal_hor,posiciones,pal_ver,dic)

def imp_matriz(horizontal, posiciones, verticales, diccionario):
	return 'pepe'
		
def verticales(horizontal, diccionario, lista):
	'''recibe una palabra(horizontal) al azar, una lista con numeros ordenados y un diccionario.
	devuelve una lista de tuplas con palabras que tiene una letra en comun con la horizontal y su
	longitud que tiene arriba y abajo de esa letra'''

	keys = diccionario.keys()
	n_vert = random.sample(keys, 30) #obtiene las n palabras verticales

	list_vert = []
	if horizontal in n_vert: #borra la palabra vertical igual a la horizontal
		n_vert.remove(horizontal)
		print('hubo')

	for i in lista:
		arriba = 0
		abajo = 0
		for j in n_vert:
			if (horizontal[i] in j) and (j not in list_vert): #si una cumple pasa a la siguiente iteracion
				for c in range(len(j)):
					if c == horizontal[i]:
						continue
					pos = j.index(horizontal[i])
					if c < pos:
						arriba += 1
					if c > pos:
						abajo +=1
				list_vert.append((j,arriba,abajo))
				break
	print(horizontal,lista)
	print(list_vert)
	return list_vert
def horizontal(palabras):
	'''recibe un diccionario, busca cual de ella tiene una longitud mayor igual a 8
	y elige una de ellas.
	devuelve la palabra horizontaly una lista de numeros a distancia 2 y 3'''
	horizontales = []
	keys = palabras.keys()
	for palabra in keys:
		if len(palabra) >= 8:
			horizontales.append(palabra)
	p_alea =random.choice(horizontales)

	nueva_list = []
	#genera una lista con numeros distanciados 2 o 3 numero entre ellos
	while True:
		if not nueva_list:
			nueva_list.append(random.randint(0,1))
		num_alea = random.randint(2,3)
		num_app = nueva_list[-1] + num_alea
		if num_app <= (len(p_alea)-1):
			nueva_list.append(num_app)
		else:
			break
		if len(nueva_list) == int(len(p_alea)/2):
			break
	return p_alea, nueva_list 

def manejo_archivo(archivo):
	'''recibe el archivo que contiene muchas palabras y las guarda en un diccionario 
	separando palabra y descripcion'''
	dic = {}
	with open(archivo, encoding= "utf8") as palabras:
		for line in palabras:
			palabra, descripcion = line.rstrip('\n').split('|')
			if not palabra in dic:
				dic[palabra] = descripcion
		return dic
		

main()
