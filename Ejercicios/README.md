# Python

Python es un lenguaje de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código.​ Se trata de 
un lenguaje de programación multiparadigma, ya que soporta orientación a objetos, programación imperativa y, en menor medida, 
programación funcional.

### Instalación de herramientas en Ubuntu
- La consola / terminal / línea de comandos
- El editor de código: Visual Studio Code
- El lenguaje de programación: Python

Instalación de la consola
- En Ubuntu no necesitas instalar una consola a diferencia de Windows. Para poder usar la terminal debes presionar Ctrl + Alt + t y voilà, se abrirá frente a tus ojos

Instalación del editor de código
- Abre tu navegador preferido (Firefox, Chrome, el que quieras) y dirígete a https://go.microsoft.com/fwlink/?LinkID=760868
- Abre el archivo descargado. Notarás que termina en “.deb”
- Sigue los pasos de instalación
- Introduce la contraseña de tu sistema:
- Espera a que termine la instalación:
- Instalación finalizada:

Instalación de Python
Abre tu terminal y ejecuta los siguientes comandos:
```sh
sudo apt update
```
```sh
sudo apt install python3-pip
```
- Te mostrará si deseas continuar con la instalación, da click en enter.
- La instalación empezará:
- Ejecuta el comando python3 -V para verificar que el lenguaje de programación se instaló correctamente


### Instalación en herramientas en Mac
- La consola / terminal / línea de comandos
- El editor de código: Visual Studio Code
- El lenguaje de programación: Python

Instalación de la consola
> En Mac no necesitas instalar una consola a diferencia de Windows. Sin embargo, para poder usar correctamente la terminal debes seguir una serie de pasos:
- 1 Abre la carpeta Aplicaciones. Luego, ve a Utilidades y haz doble click en la aplicación Terminal. Esto debería abrirte la consola de comandos. Si no te funcionó o no encontraste la aplicación de Terminal, puedes pulsar ⌘ + barra espaciadora para abrir Spotlight. Allí escribe “Terminal” y haz click en el primer resultado de búsqueda.

Ejecuta los siguientes comandos:
```sh
sudo xcode-select --install
sudo xcode-select --reset
```
- La Terminal te pedirá que ingreses la contraseña de administrador de tu computadora. Házlo.
- Una vez que completes los dos pasos anteriores, tu terminal debería funcionar a la perfección.
- 
Instalación del editor de código
- 1 Abre tu navegador preferido (Safari, Chrome, el que quieras) y dirígete a https://code.visualstudio.com/
- Una vez allí, haz click en el botón “Download for Mac” o “Descargar para Mac”
- Abre la lista de archivos descargados de tu navegador, y encuentra el instalador
- Arrastra el archivo Visual Studio Code.app a la carpeta Aplicaciones
- 5.Añade el editor al dock dándole click derecho al ícono que te aparece en pantalla y seleccionando “Options” u “Opciones”, y luego “Keep in dock” o “Mantener en el dock”

Instalación de Python
- Abre tu navegador preferido (Safari, Chrome, el que quieras) y dirígete a https://www.python.org/downloads/
- Da click en el botón “Download Python 3.x.x”. En las “x” vas a ver números. Lo importante es que el primer número sea un 3, los dos que siguen no nos interesan, porque cambian todo el tiempo.
- Abre el instalador descargado, y sigue los pasos



### Operadores aritméticos

> Orden de las operaciones PEMDAS: Parentesis, exponentes, multiplicación, división, adicción y substración.

| Operadores aritméticos | README |
| ------ | ------ |
| 5 + 5 | Adición (Suma) |
| 5 - 5 | sustracción (Resta) |
| 5 * 5 | Multiplicación |
| 5 / 5 | División (con decimales) |
| 5 // 5 | División (sin decimales) |
| 21 % 5 | Resto de la división |
| 2 ** 2 | Potenciación |
| 8**(1/3) | Raíz cuadrada |

#### ¿Qué es una variable?
Es un lugar en memoria (una especie de caja) en el que podemos guardar objetos (números, texto, etc). Esta variable posee un identificador o nombre con el cual podemos llamarla cuando la necesitemos.
> No pueden empezar con un número.
> Deben estar en minúsculas
> Para separar las palabras usamos el guion bajo: _
> Estas reglas son aplicadas al lenguaje python, en otros lenguajes pueden haber otras reglas.

- Asignación de variables con su edentificador o nombre
```sh
nombreDeLaVariable
```
- Asignándole un valor a la variable
```sh
nombreDeLaVariable = 15
```
Reasignación de variables
```sh
edad = 15
edad = 46
```
## Tipos de datos simples
| Dato | Significado |
| ------ | ------ |
| int | entero |
| real | float |
| bool | booleano |
| char | string |

## Tipos de datos Compuestos

| Dato | Significado |
| ------ | ------ |
| Tablas, arrays y string | sinNotas |
| Estructura y record | sinNotas |
| Tupla string(statico, inmutable) | sinNotas |
| Listas, diccionarios, set (dinamico, mutable) | sinNotas |

int
```sh
edad = 55
```
float
```sh
precioPan = 2.50
```
bool
```sh
casado = true
```
char
```sh
miPrimerPrograma = "Hola Mundo"
```
Concatenar variables
```sh
nombre = "luis"
apellido = "morales"
print(nombre + " " + apellido)
```
### Funciones
Para pedirle al usuario que introduzca datos
```sh
Input("")
```
String convertirlo a número entero.
```sh
int()
```
Convertir números tanto decimales como enteros a strings.
```sh
str()
```
### Convertir un dato a un tipo diferente
Convertir string a int
```sh
numero = input("escrive tu edad")
numero1 = input("escrive tu edad")
numero = int(numero)
numero1 = int(numero1)
numero + numero1
```
Convertir de int a string

```sh
edad = 55
str(edad)
```

### Operadores lógicos y de comparación

| Operadores lógicos | Significado |
| ------ | ------ |
| and  | Para comparar si dos valores son verdaderos. |
| or |  Si al menos una de tus variables cuenta con los requisitos que buscas. |
| not  |  Para invertir el valor booleano. |


| Operadores comparación | Significado |
| ------ | ------ |
| ==  |  Compara dos valores y te dice si son iguales o no. |
| != | Compara dos valores y te dice sin son diferentes o no. |
| > | Compara si es mayor que otro valor. |
| < | Compara si es menor que otro valor. |
| >= | Igual o mayor que el valor a comparar. |
| <= | Igual o menor que el valor a comparar. |

### Ejemplos
```sh
estudia = True
trabaja = False
estudia and trabaja
```
```sh
estudia = True
trabaja = False
estudia or trabaja
```
```sh
estudia = True
not estudia
```

