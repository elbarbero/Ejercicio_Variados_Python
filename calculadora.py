from tkinter import *

def numberPressed(arg):
	global campo
	global number
	global signo
	try:
		if arg != '.' or len(campo.get().split('.'))==1:
			campo.set(campo.get() + arg)
			number = float(campo.get())
			operaciones(signo)
	except ValueError as ex:
		campo.set("error")
		print(type(ex).__name__)

def MasMenosPressed():
	global campo
	global number
	global signo
	valor = DoubleVar(value=campo.get())
	campo.set(campo.get().replace('-','') if len(campo.get().split('-')) == 2 else "-"+campo.get())
	print('*****',campo.get())
	number = float(campo.get())
	print('#####',number)
	operaciones(signo)

def operaciones(arg):
	global number
	global resultado
	global signo
	try:
		if arg=='+':
			resultado += number
		elif arg=='-':
			resultado -= number
		elif arg=='÷':
			resultado /= number
		elif arg=='x':
			resultado *= number
		elif arg=='':
			resultado = number
	except Exception as ex:
		campo.set("error")
		print(type(ex).__name__)


def signoPressed(arg):
	global signo
	global number, resultado
	signo = arg
	if arg=='C':
		resultado = 0
		number = 0
		signo = ''
	elif arg=='CE':
		number = 0

	campo.set("" if arg != '=' else resultado)

root = Tk()
campo = StringVar()
resultado = 0
number = 0
signo = ''

entry = Entry(root, textvariable=campo)

entry.grid(row=0, column=0, columnspan=5, rowspan=2, padx=5, pady=5, sticky=N+S+E+W)
entry.config(justify="right", state="disabled")

boton = Button(root, text="+/-", width=10, height=3, command=MasMenosPressed)
boton.grid(row=6, column=0)
boton = Button(root, text="0", width=10, height=3, command=lambda: numberPressed('0'))
boton.grid(row=6, column=1)
boton = Button(root, text=".", width=10, height=3, command=lambda: numberPressed('.'))
boton.grid(row=6, column=2)
boton = Button(root, text="=", width=10, height=3, command=lambda: signoPressed('='))
boton.grid(row=6, column=3)

# ----------------------------------------------

boton = Button(root, text="1", width=10, height=3, command=lambda: numberPressed('1'))
boton.grid(row=5, column=0)
boton = Button(root, text="2", width=10, height=3, command=lambda: numberPressed('2'))
boton.grid(row=5, column=1)
boton = Button(root, text="3", width=10, height=3, command=lambda: numberPressed('3'))
boton.grid(row=5, column=2)
boton = Button(root, text="+", width=10, height=3, command=lambda: signoPressed('+'))
boton.grid(row=5, column=3)

# ----------------------------------------------

boton = Button(root, text="4", width=10, height=3, command=lambda: numberPressed('4'))
boton.grid(row=4, column=0)
boton = Button(root, text="5", width=10, height=3, command=lambda: numberPressed('5'))
boton.grid(row=4, column=1)
boton = Button(root, text="6", width=10, height=3, command=lambda: numberPressed('6'))
boton.grid(row=4, column=2)
boton = Button(root, text="-", width=10, height=3, command=lambda: signoPressed('-'))
boton.grid(row=4, column=3)

# ----------------------------------------------

boton = Button(root, text="7", width=10, height=3, command=lambda: numberPressed('7'))
boton.grid(row=3, column=0)
boton = Button(root, text="8", width=10, height=3, command=lambda: numberPressed('8'))
boton.grid(row=3, column=1)
boton = Button(root, text="9", width=10, height=3, command=lambda: numberPressed('9'))
boton.grid(row=3, column=2)
boton = Button(root, text="x", width=10, height=3, command=lambda: signoPressed('x'))
boton.grid(row=3, column=3)

# ----------------------------------------------

boton = Button(root, text="1/x", width=10, height=3)
boton.grid(row=2, column=0)
boton = Button(root, text="CE", width=10, height=3, command=lambda: signoPressed('CE'))
boton.grid(row=2, column=1)
boton = Button(root, text="C", width=10, height=3, command=lambda: signoPressed('C'))
boton.grid(row=2, column=2)
boton = Button(root, text="÷", width=10, height=3, command=lambda: signoPressed('÷'))
boton.grid(row=2, column=3)

root.mainloop()