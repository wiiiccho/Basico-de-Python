# Un diccionario es una estructura de datos de llaves y valores
def run():
	miDiccionario = {
		"llave": 1,
		"llave1": 2,
		"llave2": 3
	}
	# print(miDiccionario)
	# print(miDiccionario["llave"])
	# print(miDiccionario["llave1"])
	# print(miDiccionario["llave2"])

	# keys() metodo del diccionario que me debuelve las llaves
	# for llaves in miDiccionario.keys():
	# 	print(llaves)
	
	# el metodo values() lo que hace es devolver los valores del diccionario
	# for llaves in miDiccionario.values():
	# 	print(llaves)

	# items() me debuelve las llaves y el valor del diccionario
	for llaves, valores in miDiccionario.items():
		print(llaves + " Tien el valor de " + str(valores))

if __name__ == "__main__":
	run()
