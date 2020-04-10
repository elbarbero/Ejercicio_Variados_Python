
class Categoria():

	def __init__(self, nombre, sueldoBase, precioHoraExtra):
		self.nombre = nombre
		self.sueldoBase = sueldoBase
		self.precioHoraExtra = precioHoraExtra

	def __str__(self):
		return f"La categoria {self.nombre} tiene un sueldo base de {self.sueldoBase} € y la hora extra se paga a {self.precioHoraExtra} €/h"


class Empleado():

	def __init__(self, nombre, categoria, nHorasExtra):
		self.nombre = nombre
		self.categoria = categoria
		self.nHorasExtra = nHorasExtra
		self.calcularSueldo()
	def calcularSueldo(self):
		self.sueldoTotal = self.categoria.sueldoBase + ( self.categoria.precioHoraExtra * self.nHorasExtra )

	def __str__(self):
		return f"El empleado {self.nombre} pretenece a la categoría {self.categoria.nombre} y ha hecho {self.nHorasExtra} horas extra"


class Empresa():

	def __init__(self, nombre, empleados):
		self.nombre = nombre
		self.empleados = empleados

	def __str__(self):
		return f"La empresa {self.nombre} tiene un total de {len(self.empleados)} empleados"




categorias = [
			Categoria(nombre = 'Administrativo', sueldoBase = 200, precioHoraExtra = 20),
			Categoria(nombre = 'Programador', sueldoBase = 220, precioHoraExtra = 30),
			Categoria(nombre = 'Analista', sueldoBase = 250, precioHoraExtra = 40),
			Categoria(nombre = 'Analista-Programador', sueldoBase = 300, precioHoraExtra = 50)
			]
[print(c) for c in categorias]

empleados = [
			Empleado(nombre = 'Jaimito', categoria = categorias[2], nHorasExtra = 7),
			Empleado(nombre = 'Luis', categoria = categorias[1], nHorasExtra = 10),
			Empleado(nombre = 'Lucía', categoria = categorias[0], nHorasExtra = 0),
			Empleado(nombre = 'Alba', categoria = categorias[3], nHorasExtra = 5),
			Empleado(nombre = 'Mario', categoria = categorias[1], nHorasExtra = 9),
			]
[print (e) for e in empleados]

miEmpresa = Empresa(nombre = "Informatica SL", empleados = empleados)
print(miEmpresa)

print("******************************** INFORME DE EMPLEADOS ********************************")
print("CATEGORÍA\t\t\tNOMBRE MEPLEADO\t\t\tTOTAL HORAS\t\t\tSUELDO A PERCIBIR")
[print(e.categoria.nombre, "\t\t\t", e.nombre, "\t\t\t", e.nHorasExtra, "\t\t\t", e.sueldoTotal, '€') for e in miEmpresa.empleados]