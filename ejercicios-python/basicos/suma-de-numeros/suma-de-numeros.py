while True:
	n = int(input("Number:"))  # Pedimos el número

	if n == 0: # Le decimos que si el numero es cero, diga que el numero no es válido, ya que imprimiriamos numeros negativos o ningún número
		print("Invalid number")

	if n > 0: # Le decimos que si el número es válido (mayor a 0), siga con el programa.
		break


while True:
	n = n-1 # Le decimos que n va a ser igual a el número -1
	print(n)
	if n == 0: # Le decimos que cuando n sea 0, que el bucle se pare, y por tanto se parará el programa.
		break
