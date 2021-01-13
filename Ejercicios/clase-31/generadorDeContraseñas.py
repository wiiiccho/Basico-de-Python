import random
def generarPasword():
	mayusculas = ["A","B","C","D","E","T","G"]
	minusculas = ["a","b","c","d","r","f","g"]
	simbolo = ["!", "#", "="]
	numeros = ["1","2", "3", "4"]
	caracteres = mayusculas + minusculas + simbolo + numeros
	password = []
	for i in range(1,15):
		caracterRandom = random.choice(caracteres)
		password.append(caracterRandom)
	password = ''.join(password)
	return password



def run():
	password = generarPasword()
	print("Tu nueva contraseña es: " + password)




if __name__ == "__main__":
	run()