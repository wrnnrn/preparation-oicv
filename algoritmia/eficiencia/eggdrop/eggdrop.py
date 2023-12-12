huevos = 20
T = 50

print("Opciones: si, no y piso(indica que es el piso o numero)")

while True:
	print("T actual : ", round(T))
	print("Intentos (huevos)", + huevos)
	pregunta = input("¿El huevo se rompe? : ")
	
	if pregunta == 'piso':
		print("T : ", round(T))
		break

	if huevos == 0:
		print("No se ha podido hallar T")
		break

	if pregunta == 'si':
		T = T - (T / 2)
		huevos = huevos -1
	
	if pregunta == 'no':
		T = T + (T / 2)
		huevos = huevos -1

	if pregunta == '':
		print("Tienes que dar una respuesta")
