# Descargar la extencion Python para visual estudio
# Python
menu = """
Biehnvenido al conversor de monedas 
1- Quetzlses Guatemaltecos
2- pedos argentinos
3- pedos mexicanos
Elige una opcion :
"""
opciones = int(input(menu))
if opciones == 1:
	quetzales = input("¿Cuantos quetzales tienes?: ")
	quetzales = float(quetzales)
	valorDolar = 7
	dolares = quetzales / valorDolar
	# Quitamos los desimales y indicamos la cantidad de desimales que yo quiero
	dolares = round(dolares, 2)
	dolares = str(dolares)
	print("Tienes $ " + dolares + " dolares")
elif opciones == 2:
	pesos = input("¿Cuantos pesos argentinos tienes?: ")
	pesos = float(pesos)
	valorDolar = 65
	dolares = pesos / valorDolar
	# Quitamos los desimales y indicamos la cantidad de desimales que yo quiero
	dolares = round(dolares, 2)
	dolares = str(dolares)
	print("Tienes $ " + dolares + " dolares")
elif opciones == 3:
	pesos = input("¿Cuantos pesos mexicanos tienes?: ")
	pesos = float(pesos)
	valorDolar = 24
	dolares = pesos / valorDolar
	# Quitamos los desimales y indicamos la cantidad de desimales que yo quiero
	dolares = round(dolares, 2)
	dolares = str(dolares)
	print("Tienes $ " + dolares + " dolares")
else:
	input("Ingresa un opcion correrta forfavor")


# Ejecutar un archivo Python
# Debemos de estar fuera de Python para que se ejecute
# python convertidorDolar.py