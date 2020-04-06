from io import open

try:
	fichero = open("contador.txt", 'r')
	contenido = fichero.readline()
	contador = int( contenido )
except FileNotFoundError:
	print("Fichero no econtrado.")
	fichero = open("contador.txt", 'a+')
	fichero.write('0')
	contador = 0

fichero.close()

visita = input( 'Viene o se va?')

if visita == 'inc':
	fichero = open("contador.txt", 'w')
	fichero.write(str(contador+1))
elif visita == 'dec':
	fichero = open("contador.txt", 'w')
	fichero.write(str(contador-1))
else:
	contenido = open("contador.txt", 'r').readline()
	print(contenido)

fichero.close()