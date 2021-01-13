# Pedimos al usuario un valor lo convertimos de string a float y lo guardamos en la variable quetzales
quetzales = float(input("¿Cuantos Quetzales tienes?: "));

valorDolar = 7

dolares = quetzales / valorDolar
# Quitamos los desimales y indicamos la cantidad de desimales que yo quiero
# round(variable, cantidadDeDesimalesQueYoQuiero)
dolares = round(dolares, 2)


# Dos formas para mostrarlo al usuario

# 1
# Lo debemos convertimos de float a string
# dolares = str(dolares)
# print("Tienes $ " + dolares + " dolares");

# 2
print('Tienes $ {0} dolares'.format(dolares));
