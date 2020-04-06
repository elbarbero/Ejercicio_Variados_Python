from io import open

dic_personas = {}
personas = []

fichero = open('personas.txt', 'r')

for p in fichero.readlines():
	l = p.replace("\n", "").split(";")
	dic_personas = {"id":l[0], "nombre":l[1], "apellido":l[2], "nacimiento":l[3]}
	personas.append(dic_personas)

for k, v in dic_personas.items():
	print(k, v)

print(dic_personas)
print(personas)
