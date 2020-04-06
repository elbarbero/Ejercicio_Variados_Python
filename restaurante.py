import sqlite3 as sql

conexion = None
cursor = None

def crear_db():
	global conexion
	global cursor

	conexion = sql.connect("restaurante.db")
	try:
		cursor = conexion.cursor()
		cursor.execute("""
			CREATE TABLE categoria(
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			nombre VARCHAR(100) UNIQUE NOT NULL)
			""")
		cursor.execute("""
			CREATE TABLE plato(
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			nombre VARCHAR(100) UNIQUE NOT NULL, 
			categoria_id INTEGER NOT NULL,
			FOREIGN KEY(categoria_id) REFERENCES categoria(id))
			""")
	except sql.OperationalError as ex:
		print(type(ex).__name__)
		print("Las tablas ya existen")
	else:
		print("Tablas creadas correctamente")


def agregar_categoria():
	try:
		nomCat = input("->Introduce el nombre la categoría: ")
		cursor.execute("INSERT INTO categoria VALUES (null, '{}')".format(nomCat))
		conexion.commit()
	except sql.IntegrityError as ex:
		print(type(ex).__name__)
		print("La categoría {} ya existe. Inserte otra distinta".format(nomCat))


def agregar_plato():
	cursor.execute("SELECT * FROM categoria")
	categorias = cursor.fetchall()
	if len(categorias) > 0:
		for cat in categorias:
			print(cat[0], ' - ', cat[1])
		idcat = input("->Elija una categoría para meter los platos: ")
		print(idcat)
		if idcat != '':
			try:
				nomPlat = input("->Introduce el nombre del plato: ")
				cursor.execute("INSERT INTO plato VALUES (null, '{}',{})".format(nomPlat, idcat))
				conexion.commit()
			except sql.IntegrityError as ex:
				print(type(ex).__name__)
				print("El plato {} ya existe. Inserte otro distinta".format(nomPlat))


def mostrar_menu():
	cursor.execute("SELECT * FROM categoria")
	categorias = cursor.fetchall()

	cursor.execute("SELECT * FROM plato")
	platos = cursor.fetchall()

	print("------------MENÚ------------\n")
	for categoria in categorias:
		print(categoria[1].upper())
		for plato in platos:
			if plato[-1] == categoria[0]:
				print(" - {}".format(plato[1]))


def iniciar():
	while(True):
		print("------------ELEGIR OPCIÓN------------\n",
		"1-Crear una categoría\n",
		"2-Crear un plato\n",
		"3-Salir")
	
		option = int( input("->Seleccione opción: ") )
		if option == 1:
			agregar_categoria()
		elif option == 2:
			agregar_plato()
		elif option == 3:
			mostrar_menu()
			break


crear_db()
iniciar()
conexion.close()