def esPrimo(numero):
	contador = 0
	# numero + 1 es para asegurarmos que lleguemos al numero que el usuario ingreso
	for i in range(1,numero + 1):
		if i == 1 or i == numero:
			continue
		if numero % i == 0:
			contador = contador + 1
	if contador == 0:
		return True
	else:
		return False


def run():
	numero = int(input("Escribe un numero: "))
	# el resultado de la funcio igual a True 
	if esPrimo(numero):
		print("Es primo")
	else:
		print("No es primo")



if __name__ == "__main__":
	run()