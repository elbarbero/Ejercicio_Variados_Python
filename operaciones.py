def suma(num1, num2):
	try:
		return num1 + num2
	except TypeError as ex:
		print(type(ex).__name__,'- {}'.format("Tipo de dato no valido"))

def resta(num1, num2):
	try:
		return num1 + num2
	except TypeError as ex:
		print(type(ex).__name__,'- {}'.format("Tipo de dato no valido"))

def producto(num1, num2):
	try:
		return num1 * num2
	except TypeError as ex:
		print(type(ex).__name__,'- {}'.format("Tipo de dato no valido"))

def division(num1, num2):
	try:
		return num1 / num2
	except TypeError as ex:
		print(type(ex).__name__,'- {}'.format("Tipo de dato no valido"))
	except ZeroDivisionError as ex:
		print(type(ex).__name__,'- {}'.format("No se puede dividir por cero"))

