import time, serial, io, threading
from tkinter import *
from tkinter import messagebox as MessageBox


threads = []
board = serial.Serial("COM3", baudrate=115200, timeout=1)
statusLed = '0'

def openPort():
	global board
	if not board.is_open:
		board = serial.Serial("COM3", baudrate=115200, timeout=1)
		texto.insert(END,"\n"+ "---------PUERTO ABIERTO---------")

def readPort():
	global threads
	if board.is_open:
		t = threading.Thread(target=worker)
		threads.append(t)
		t.start()
	#print(threading.currentThread().getName())

def worker():
	global board, statusLed
	try:
		while True:
			time.sleep(2)
			statusLed = board.readline().rstrip(b'\r\n')
			statusLed = 0 if statusLed == b'' else statusLed
			print(statusLed)
			texto.insert(END,"\n"+ str(statusLed))
	except serial.SerialException as ex:
		print(type(ex).__name__)
		MessageBox.showinfo("Puerto COM","Debe abrir antes el puerto COM")

def closePort():
	global board
	if board.is_open:
		board.flushInput()
		board.flushOutput()
		board.close()
		texto.insert(END,"\n"+ "---------PUERTO CERRADO---------")
		threads[0].do_run = False
	else:
		MessageBox.showinfo("Puerto COM","El puerto COM ya está cerrado")

def led():
	global statusLed
	if board.is_open:
		if int(statusLed) == 0:
			led = '1'
			texto.insert(END,"\n"+ "- Led ON")
		else:
			led = '0'
			texto.insert(END,"\n"+ "- Led OFF")
		#board.write(str(led).encode())
		board.write(led.encode())
		statusLed = led
		#print(led)
		#statusLed = board.readline().rstrip(b'\r\n')
		#rint(statusLed)
	else:
		MessageBox.showinfo("Puerto COM","El puerto COM está cerrado")



root = Tk()

root.title("ARDUINO")
root.geometry("500x500")

frame = Frame(root)
frame.pack(side="left")

imagen = PhotoImage(file="arduino.gif")
label = Label(root, image=imagen, bd=0).pack(side="top")

Button(frame, text="Abrir Puerto", command=openPort).pack()
Button(frame, text="Leer Puerto", command=readPort).pack()
Button(frame, text="Cerrar Puerto", command=closePort).pack()
Button(frame, text="LED", command=led).pack()


texto = Text(root)
texto.pack()
texto.config(width=30, height=10, font=("Consolas",12), padx=15, pady=15, selectbackground="red")

root.mainloop()



