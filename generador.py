import math
import random

def leer_numero(ini, fin, mensaje):
	while True:
		try:
			valor = int( input(mensaje) )
		except TypeError as ex:
			print(type(ex).__name__,'- {}'.format("Tipo de dato no valido"))
		else:
			if valor >= ini and valor <= fin:
				break
	return valor


def generador():
	numeros = leer_numero(1,20,"¿Cuantos números quieres generar? [1-20]: ")
	modo = leer_numero(1,3,"¿Cómo quieres redondear los números? " \
                           "[1]Al alza [2]A la baja [3]Normal: ")
	lista = []

	for i in range(numeros):
		n = random.uniform(1, 101)
		if modo == 1:
			print("{} => {}".format(n, math.ceil(n)) )
			n = math.ceil(n)
		elif modo == 2:
			print("{} => {}".format(n, math.floor(n)) )
			n = math.floor(n)
		elif modo == 3:
			print("{} => {}".format(n, round(n,2)) )
			n = round(n,2)
		lista.append(n) # Entero aleatorio de 1 a 100, 101 excluído

	print(lista)

generador()