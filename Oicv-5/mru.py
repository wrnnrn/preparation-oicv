# xf = xo + v * t
print("1 - Calcular posición final")
print("2 - Calcular posición inicial")
print("3 - Calcular velocidad")
print("4 - Calcular tiempo")
calcular = int(input("Número: "))

if calcular == 1:
	print("")
	print("P.FINAL")
	pinicial = int(input("Posición inicial (m) : "))
	velocidad = int(input("Velocidad constante (m/s) : "))
	tiempo = int(input("Tiempo (seg) : "))

	calculador = velocidad * tiempo + pinicial
	print(calculador)

if calcular == 2:
	print("")
	print("P.Inicial")
	pfinal = int(input("Posición final (m) : "))
	velocidad = int(input("Velocidad constante (m/s) : "))
	tiempo = int(input("Tiempo (seg) : "))

	calculador = pfinal - velocidad / tiempo
	print(calculador)

if calcular == 3:
	print("")
	print("VELOCIDAD")
	pfinal = int(input("Posición final (m) : "))
	pinicial = int(input("Posicion inicial (m) : "))
	tiempo = int(input("Tiempo (seg) : "))

	calculador = pfinal - pinicial / tiempo
	print(calculador)
	
if calcular == 4:
	print("")
	print("TIEMPO")
	pfinal = int(input("Posición final (m) : "))
	pinicial = int(input("Posicion inicial (m) : "))
	velocidad = int(input("Velocidad (m/s) : "))

	calculador = pfinal - pinicial / velocidad
	print(calculador, "seg")
	