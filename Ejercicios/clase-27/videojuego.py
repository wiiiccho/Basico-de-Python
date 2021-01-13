# modulo es un paquete de codigo escrito por las personas que isieron python que son funciones
# y lo hacemos de esta manera
import random


def run():
					# generame un numero aleatorio entero desde el numero 1 al 100
	numeroAleatorio = random.randint(1,100)
	numeroElige = int(input("Elige un numero del 1 al 100: "))
	while numeroElige != numeroAleatorio:
		if numeroElige < numeroAleatorio:
			print("Busca un numero mas grande")
		else:
			print("Busca un numero mas pequeño")
		numeroElige = int(input("Elige otro numeor: "))
	print("Ganaste")



if __name__ == "__main__":
	run()