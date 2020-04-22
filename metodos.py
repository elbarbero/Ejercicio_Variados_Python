"""Modulo con varios métodos generales"""

def validateName(name, minC, maxC):
	"""Método que validate el nombre se usuario
		* name -> nombre a validar
		* minC -> mínimos caracteres permitidos
		* maxC -> máximos caracteres permitidos
		* return True o False
	"""
	try:
		if len(name) >= minC:
			if  len(name) <= maxC:
				if name.isalnum():
					return True
				else:
					print('El nombre {} no cumple los requisitos. Solo puede contener letras y números'.format(name))
					return False
			else:
				print('El nombre {} no cumple los requisitos. No puede contener más de {} caracteres'.format(name, maxC))
				return False
		else:
			print('El nombre {} no cumple los requisitos. Debe contener al menos {} caracteres'.format(name, minC))
			return False
	except (TypeError, Exception) as ex:
		print(type(ex).__name__, '->', ex)
		print(printExceptionMessage())
		return False


def validatePassword(password, length):
	"""Método que validate una contraseña
		* password -> contraseña a validar
		* length -> longitud mínima permitida para la contraseña
		* return True o False
	"""
	try:
		if len(password) >= length and (not ' ' in password and 
			True in containsLowerCase(password) and True in containsUpperCase(password) and 
			True in containsNumbers(password) and True in containsAlphanumeric(password)):
			return True
		else:
			print('La contraseña {} no es segura. Debe contener a menos {} caracteres, letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico'.format(password, length))
			return False
	except (TypeError, Exception) as ex:
		print(type(ex).__name__, '->', ex)
		print(printExceptionMessage())
		return False

containsLowerCase = lambda cadena: [ True if c.islower() else False for c in cadena]
containsUpperCase = lambda cadena: [ True if c.isupper() else False for c in cadena]
containsNumbers = lambda cadena: [ True if c.isnumeric() else False for c in cadena]
containsAlphanumeric = lambda cadena: [ True if not c.isalnum() else False for c in cadena]

def reverseString(cadena):
	"""Se invierte el orden de la cadena
		* cadena -> String a invertir el orden
		* return la cadena invertida
	"""
	return cadena[::-1]

def EsPar_Numero(numero):
	"""Comprueba si el número es par o impar
		* numero -> el número a comprobar
		* return True o False
	"""
	try:
		return True if numero % 2 == 0 else False
	except TypeError as ex:
		print(type(ex).__name__, '->', ex)
		print(printExceptionMessage())
		return False

def EsPar_Lista(numeros):
	"""Comprueba si los números de una lista son par
		* numeros -> lista con todos los numeros a comprobar
		* yield cada numero par
	"""
	try:
		for n in numeros:
			if n % 2 == 0:
				yield n
	except TypeError as ex:
		print(type(ex).__name__, '->', ex)
		print(printExceptionMessage())

def EsImpar_Lista(numeros):
	"""Comprueba si los números de una lista son impar
		* numeros -> lista con todos los numeros a comprobar
		* yield cada numero impar
	"""
	try:
		for n in numeros:
			if n % 2 != 0:
				yield n
	except TypeError as ex:
		print(type(ex).__name__, '->', ex)
		print(printExceptionMessage())

def printExceptionMessage():
	"""
		Metodo para mostrar un mensaje de error según la excepción producida
			* return el mensaje a mostrar
	"""
	import sys, traceback
	exc_type, exc_value, exc_traceback = sys.exc_info()
	track = traceback.format_exception(exc_type, exc_value, exc_traceback)
	return traceback.print_exception(exc_type, exc_value, exc_traceback, limit=2, file=sys.stdout)

def convertStringToByte(*args):
	"""Convierte un String a Byte
		* args -> n argumentos que se quieren convertir a Byte
		* yield argumento ya convertido en un generator object
	"""
	for arg in args:
		try:
			yield str(arg).encode()
		except Exception as ex:
			print(printExceptionMessage())

def convertByteToString(*args):
	"""Convierte un Byte a String
		* args -> n argumentos que se quieren convertir a String
		* yield argumento ya convertido en un generator object
	"""
	for arg in args:
		try:
			yield arg.decode()
		except Exception as ex:
			print(printExceptionMessage())


