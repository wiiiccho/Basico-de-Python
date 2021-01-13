# Descargar la extencion Python para visual estudio
# Python

valorDolarGuatemala = 7;
valorDolarColombia = 385;
valorDolarmexico = 24;

def conversor(tipoPesos, valorDolar):
	tipoValor = int(input("¿Cuantos pesos " + tipoPesos + " tienes?: "))
	tipoValor = float(tipoValor)
	dolares = tipoValor / valorDolar
	# Quitamos los desimales y indicamos la cantidad de desimales que yo quiero
	dolares = round(dolares, 2)
	dolares = str(dolares)
	print("Tienes $ " + dolares + " dolares")


menu = """
Biehnvenido al conversor de monedas 
1- Quetzlses Guatemaltecos
2- pedos argentinos
3- pedos mexicanos
Elige una opcion :
"""
opciones = int(input(menu))
if opciones == 1:
	conversor("Guatemalteco", valorDolarGuatemala);
elif opciones == 2:
	conversor("Colombiano", valorDolarColombia);
elif opciones == 3:
	conversor("Mexicano", valorDolarmexico);
else:
	input("Ingresa un opcion correrta forfavor")


# Ejecutar un archivo Python
# Debemos de estar fuera de Python para que se ejecute
# python convertidorDolar.py