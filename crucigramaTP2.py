import csv
import random
import argparse

def main():

	parser = argparse.ArgumentParser(description='crucigramaTP2')
	parser.add_argument('-s', '--solucion', action='store_true', help='imprimir la solucion')
	args = parser.parse_args()

	imprimir_solucion = args.solucion # es True si el usuario incluyó la opción -s

	dic = manejo_archivo('palabras.csv')
	palab_hor,posiciones = horizontal(dic)
	palab_verticales = verticales(palab_hor, dic, posiciones)
	long_matriz(palab_hor,posiciones,palab_verticales)
	imp_matriz(palab_hor,posiciones,palab_verticales,dic)

def imp_matriz(horizontal, posiciones, verticales, diccionario):
	return 'pepe'

def long_matriz(horizontal,posiciones,verticales):
	'''calcula la longutid de cada palabra apartir de la posicion de cruce con la 
	horizontal y devuelve una tupla'''
	longitudes = []
	for i in range(len(posiciones)):
		arriba = 0
		abajo = 0
		for c in range(len(verticales[i])):
			if verticales[i][c] == horizontal[posiciones[i]]:
				continue
			pos = verticales[i].index(horizontal[posiciones[i]])
			if c < pos:
				arriba += 1
			if c > pos:
				abajo += 1
		longitudes.append((verticales[i], arriba, abajo))
	print(longitudes)
	return longitudes
def verticales(horizontal, diccionario, lista):
	'''recibe una palabra(horizontal) al azar, una lista con numeros ordenados y un diccionario.
	devuelve una lista con palabras que tiene una letra en comun con la horizontal'''

	keys = list(diccionario.keys())

	list_vert = []
	cont = 0
	while True:
		p_alea = random.choice(keys)
		if p_alea == horizontal:
			continue
		if (horizontal[lista[cont]] in p_alea) and (p_alea not in list_vert):
			list_vert.append(p_alea)
			cont +=1
		if len(list_vert) == len(lista):
			break
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
	print(p_alea,nueva_list)
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
