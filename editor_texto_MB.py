from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog
from io import open

ruta = '';
files = [("Todos los ficheros", '*.*'),  
             ('Archivos de Python', '*.py'), 
             ("Fichero de texto", '*.txt')] 

# Métodos
def btnNewClick(event=None):
	texto.delete("1.0","end")

def btnOpenClick(event=None):
	global ruta
	ruta = FileDialog.askopenfilename(title="Abrir un fichero", initialdir="Documentos", 
		filetypes=(("Fichero de texto","*.txt"),
			("Todos los ficheros","*.*")) )
	if ruta != '':
		fichero = open(ruta, 'r+') # modo lectura más escritura.
		contenido = fichero.read()
		btnNewClick()
		texto.insert('1.0', contenido)
		fichero.close()

def btnSaveClick(event=None):
	global ruta
	try:
		if ruta != '':
			fichero = open(ruta, 'w')
			fichero.seek(0) # Ponemos el puntero al principio
			fichero.writelines(texto.get("1.0","end"))
			fichero.close()
		else:
			btnSaveAsClick()
	except FileNotFoundError as ex1:
		print("Fichero no econtrado. No se ha podido guardar el archivo")
		print(type(ex1).__name__)
	except Exception as ex2:
		print("Ha ocurrido un a la hora de guardar el archivo")
		print(type(ex2).__name__)

def btnSaveAsClick():
	print("aqui")
	fichero = FileDialog.asksaveasfile(mode='w', defaultextension="files")
	if fichero is None: # asksaveasfile return `None` if dialog closed with "cancel".
		return
	fichero.seek(0) # Ponemos el puntero al principio
	fichero.writelines(texto.get("1.0","end"))
	fichero.close()

def btnCloseFileClick():
	global ruta
	if MessageBox.askquestion("Cerrar Fichero","¿Desea guardar antes de salir?") == "yes":
		btnSaveClick()

def btnAcercaDeClick():
	acercaDe = Toplevel(root)
	acercaDe.title("Acerca De...")
	acercaDe.resizable(0,0)
	acercaDe.geometry("200x200")
	Label(acercaDe, text="Copyrigth\nVersion Beta 0.1\nCreated by Mario").pack()

# Configuración de la raíz
root = Tk()
root.title("Mi editor")
root.geometry("500x500")

# Vertical (y) Scroll Bar
scroll = Scrollbar(root)
scroll.pack(side=RIGHT, fill=Y)

# Get screen size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

menubar = Menu(root)
root.config(menu=menubar)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo  Ctrl+N", command=btnNewClick)
filemenu.add_command(label="Abrir  Ctrl+O", command=btnOpenClick)
filemenu.add_command(label="Guardar  Ctrl+G", command=btnSaveClick)
filemenu.add_command(label="Guardar cómo", command=btnSaveAsClick)
filemenu.add_command(label="Cerrar", command=btnCloseFileClick)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Ayuda")
helpmenu.add_separator()
helpmenu.add_command(label="Acerca de...", command=btnAcercaDeClick)

menubar.add_cascade(label="Archivo", menu=filemenu)
menubar.add_cascade(label="Ayuda", menu=helpmenu)

texto = Text(root, yscrollcommand=scroll.set)
texto.pack(fill="both", expand=1) # ASI OCUPA TODO EL TAMAÑO DE LA INTERFAZ
texto.config(width=30, height=10, font=("Consolas",12), padx=5, pady=5, selectbackground="red")
texto.bind('<Control-n>',btnNewClick) # bindeo teclas para nuevo
texto.bind('<Control-o>',btnOpenClick) # bindeo teclas para abrir
texto.bind('<Control-g>',btnSaveClick) # bindeo teclas para guargar

# Finalmente bucle de la apliación
root.mainloop()