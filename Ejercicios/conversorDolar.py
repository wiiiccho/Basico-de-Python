# Descargar la extencion Python para visual estudio
# Python
quetzales = input("¿Cuantos quetzles tienes?: ")
quetzales = float(quetzales)
valorDolar = 7
dolares = quetzales / valorDolar
# Quitamos los desimales y indicamos la cantidad de desimales que yo quiero
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $ " + dolares + " dolares")


# Ejecutar un archivo Python
# Debemos de estar fuera de Python para que se ejecute
# python convertidorDolar.py