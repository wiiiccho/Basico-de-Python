# Lo que hace continue es cuando el programa se ejecute y encuentre la palabra ya no vaje para
# ejecutar las lineas de abajo si no que regrese al inicio y empieze de nuevo

# break corta el progrma o para el programa

def run():
	# for contador in range(0,1000):
	# 	if contador % 2 != 0:
	# 		continue
	# 	print(contador)


	# for i in range(0,10000):
	# 	print(i)
	# 	if i == 5000:
	# 		break



	texto = input("Escrive un texto: ")
	for i in texto:
		if i == "o":
			break
		print(i)


if __name__ == "__main__":
	run()