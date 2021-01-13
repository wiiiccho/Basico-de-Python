def run():
	# definir constantes que no cambiaran
	LIMITE = 1000
	contador = 0
	potenciaDeDos = 2**contador
	while potenciaDeDos < LIMITE:
		print("2 elevado a " + str(contador) + " es igual a " + str(potenciaDeDos))
		# evirar el bucle infinito
		contador = contador+1
		potenciaDeDos = 2**contador


if __name__ == "__main__":
	run()






# def run ():
#     CONSTANTE = 1000 #Definir constantes nombre en MAYUSCULAS
#     contador = 0
#     potencia_2 = 2**contador
#     while potencia_2 < CONSTANTE:
#         print("2 elevado a {} es igual a {}".format(contador,potencia_2))
#         contador = contador+1
#         potencia_2 = 2**contador

# if __name__ == "__main__":
#     run()