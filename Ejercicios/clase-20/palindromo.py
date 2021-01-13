# palíndromo es una palabra que se lee igual de dereccho o al revez
def palidromo(palabra):
	# remplasamos todos los espacion por un string vacio o cadena vacia
	palabra = palabra.replace(" ", "")
	palabra = palabra.lower()
	palabraInvertida = palabra[::-1]
	if palabra == palabraInvertida:
		return True
	else: 
		return False


def run():
	palabra = input("Escribe una palabra: ")
	esPalindrono = palidromo(palabra);
	if esPalindrono == True:
		print("Es palindromo")
	else:
		print("No palindromo")


if __name__ == "__main__":
	run()
