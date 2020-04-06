from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog
import sqlite3 as sql

conexion = None;
cursor = None;

root = Tk()
root.title("Menú")
root.geometry("500x700")
root.resizable(0,0)
root.config(bd=25, relief="sunken")

# Variables dinámicas
idCategoria = StringVar();
nomCategoria = StringVar();
nomPlato = StringVar();

def buscarPlatos():
	cursor.execute("SELECT * FROM categoria")
	categorias = cursor.fetchall()
	for categoria in categorias:
		idCategoria.set(categoria[0])
		nomCategoria.set(categoria[1])
		Label(root, text=nomCategoria.get(), font=("Arial",24, "bold", "underline"), padx=5, pady=20).pack(anchor="center")
		cursor.execute("SELECT * FROM plato WHERE categoria_id = {}".format(idCategoria.get()))
		platos = cursor.fetchall()
		for plato in platos:
			nomPlato.set(plato[1])
			Label(root, text=nomPlato.get(), font=("Arial",18)).pack(anchor="center")


conexion = sql.connect("restaurante.db")
cursor = conexion.cursor()

Label(root, text="Bar Casa Pepe", bg="SlateGray1", fg="blue", font=("Arial",40, "italic", "bold")).pack(anchor="center")
Label(root, text="Menú del Día", bg="SlateGray1", fg="blue", font=("Arial",30, "italic", "bold")).pack(anchor="center")

buscarPlatos()

Label(root, text="13€ (IVA Incl)", fg="MistyRose4", font=("Arial",30, "italic", "bold")).pack(side="right")

conexion.close()
root.mainloop()