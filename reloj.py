import datetime
import time
import os
import locale

locale.setlocale(locale.LC_ALL, 'es-ES') # Establece idioma en "es-ES" (español de España)

while(True):
	dt = datetime.datetime.now()
	print(dt.strftime("%A %d de %B del %Y - %H:%M:%S")) # %I 12h - %H 24h
	time.sleep(1)
	os.system('cls')


