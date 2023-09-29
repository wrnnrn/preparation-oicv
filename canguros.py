# Program from the exercises of the oicv V

#Canguro 1
pos_can_1 = int(input("Posicion inicial de canguro 1: "))
jump_can_1 = int(input("Salto canguro 1: "))

#Canguro 2
pos_can_2 = int(input("Posicion inicial de canguro 2: "))
jump_can_2 = int(input("Salto canguro 2: "))

#Conditions
can1 = pos_can_1+jump_can_1
can2 = pos_can_2+jump_can_2

#Program

if can1>can2:
	print("Alcanza? SI")
elif can2>can1:
	print("Alcanza? SI")
else:
	print("Alcanza? NO") 