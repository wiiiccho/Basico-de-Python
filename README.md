<div align="center">
  <h1>Básico de Python</h1>
</div>

<div align="center"> 
  <img src="img/python.png" width="250">
</div>

# Tabla de contenido
- [Introducción a la programación con Python](#Introducción-a-la-programación-con-Python)
    - [¿Por qué Python?](#¿Por-qué-Python?)
    - [El núcleo de un programa: los algoritmos](#El-núcleo-de-un-programa-los-algoritmos)
    - [Instalación de nuestras herramientas](#Instalación-de-nuestras-herramientas)
    - [Instalación de nuestras herramientas en Mac](#Instalación-de-nuestras-herramientas-en-Mac)
    - [Instalación de nuestras herramientas en Ubuntu](#Instalación-de-nuestras-herramientas-en-Ubuntu)






# <a name="Introducción-a-la-programación-con-Python">Introducción a la programación con Python</a>

## <a name="¿Por-qué-Python?">¿Por qué Python?</a>

#### Python funciona muy bien en estos 4 campos 

#### Internet de las cosas

-El internet de las cosas ​ es un concepto que se refiere a una interconexión digital de objetos cotidianos con internet.​​ Es, en definitiva, la conexión de internet más con objetos que con personas.​ También se suele conocer como internet de todas las cosas o internet en las cosas.

#### Inteligencia artificial 


-La inteligencia artificial (IA) es la inteligencia llevada a cabo por máquinas. En ciencias de la computación, una máquina «inteligente» ideal es un agente flexible que percibe su entorno y lleva a cabo acciones que maximicen sus posibilidades de éxito en algún objetivo o tarea.1​ Coloquialmente, el término inteligencia artificial se aplica cuando una máquina imita las funciones «cognitivas» que los humanos asocian con otras mentes humanas, como por ejemplo: «percibir», «razonar», «aprender» y «resolver problemas».

#### backend

-El back end del sitio web consiste en un servidor, una aplicación y una base de datos. Se toman los datos, se procesa la información y se envía al usuario. Los desarrolladores de Front end y Back end suelen trabajar juntos para que todo funcione correctamente.

#### Ciencia de datos

-La ciencia de datos es un campo interdisciplinario que involucra métodos científicos, procesos y sistemas para extraer conocimiento o un mejor entendimiento de datos en sus diferentes formas, ya sea estructurados o no estructurados,1​ lo cual es una continuación de algunos campos de análisis de datos como la estadística, la minería de datos, el aprendizaje automático, y la analítica predictiva.1​

#### Ventajas 
- Fácil de aprender
- Elegante
- Buenas prácticas

## <a name="El-núcleo-de-un-programa-los-algoritmos">El núcleo de un programa: los algoritmos</a>

#### ¿Qué es un Algoritmo?

En términos de programación, un algoritmo es una secuencia de pasos lógicos que permiten solucionar un problema.

#### Partes de un algoritmo
Todo algoritmo debe constar de las siguientes partes:

- Input o entrada. El ingreso de los datos que el algoritmo necesita para operar.
- Proceso. Se trata de la operación lógica formal que el algoritmo emprenderá con lo recibido del input.
- Output o salida. Los resultados obtenidos del proceso sobre el input, una vez terminada la ejecución del algoritmo.

#### ¿Para qué sirve un algoritmo?
Dicho muy llanamente, un algoritmo sirve para resolver paso a paso un problema. Se trata de una serie de instrucciones ordenadas y secuenciadas para guiar un proceso determinado.

En las Ciencias de la computación, no obstante, los algoritmos constituyen el esqueleto de los procesos que luego se codificarán y programarán para que sean realizados por el computador.

#### Características de los algoritmos

Los algoritmos presentan las siguientes características:

- Secuenciales. Los algoritmos operan en secuencia, debe procesarse uno a la vez.
- Precisos. Los algoritmos han de ser precisos en su abordaje del tema, es decir, no pueden ser ambiguos o subjetivos.
- Ordenados. Los algoritmos se deben establecer en la secuencia precisa y exacta para que su lectura tenga sentido y se resuelva el problema.
- Finitos. Toda secuencia de algoritmos ha de tener un fin determinado, no puede prolongarse hasta el infinito.
- Concretos. Todo algoritmo debe ofrecer un resultado en base a las funciones que cumple.
- Definidos. Un mismo algoritmo ante los mismos elementos de entrada (input) debe dar siempre los mismos resultados.

#### Ejemplos de algoritmos

Algoritmo para calcular el área de un triángulo rectángulo:

- INICIO
- Hallar las medidas de la base (b) y altura (h)
- Multiplicar: base por altura (b x h)
- Dividir entre 2 el resultado (b x h) / 2
- FIN

#### Diagrama de flujo

El diagrama de flujo o flujograma o diagrama de actividades es la representación gráfica de un algoritmo o proceso. Se utiliza en disciplinas como programación, economía, procesos industriales y psicología cognitiva.


<div align="center"> 
  <img src="img/Diagrama-de-flujo.jpg" width="450">
</div>


## <a name="Instalación-de-nuestras-herramientas">Instalación de nuestras herramientas</a>

```python
https://www.python.org/
```
<div align="center"> 
  <img src="img/4.png" width="450">
</div>


```python
https://cmder.net/
```
> Cmder es un programa portable para todas las versiones de Windows que se ofrece en dos variantes: Una 
> versión mínima que funciona como la terminal de Windows que ya conocemos, y una completa que, además, 
> incluye compatibilidad con comandos Unix


```python
https://code.visualstudio.com/
```
<div align="center"> 
  <img src="img/1.png" width="450">
</div>

<div align="center"> 
  <img src="img/2.png" width="450">
</div>
<div align="center"> 
  <img src="img/3.png" width="450">
</div>


## <a name="Instalación-de-nuestras-herramientas-en-Mac">Instalación de nuestras herramientas en Mac</a>

- La consola / terminal / línea de comandos
- El editor de código: Visual Studio Code
- El lenguaje de programación: Python

#### Instalación de la consola
En Mac no necesitas instalar una consola a diferencia de Windows. Sin embargo, para poder usar correctamente la terminal debes seguir una serie de pasos:

Abre la carpeta Aplicaciones. Luego, ve a Utilidades y haz doble click en la aplicación Terminal. Esto debería abrirte la consola de comandos. Si no te funcionó o no encontraste la aplicación de Terminal, puedes pulsar ⌘ + barra espaciadora para abrir Spotlight. Allí escribe “Terminal” y haz click en el primer resultado de búsqueda.

<div align="center"> 
  <img src="img/mac0.png" width="450">
</div>

#### Ejecuta los siguientes comandos:

```python
sudo xcode-select --install
sudo xcode-select --reset
```
La Terminal te pedirá que ingreses la contraseña de administrador de tu computadora. Házlo.

<div align="center"> 
  <img src="img/mac1.png" width="450">
</div>

<div align="center"> 
  <img src="img/mac2.png" width="450">
</div>


#### Instalación del editor de código

- Abre tu navegador preferido (Safari, Chrome, el que quieras) y dirígete a

```python
https://code.visualstudio.com/
```
<div align="center"> 
  <img src="img/mac3.png" width="450">
</div>

- Una vez allí, haz click en el botón “Download for Mac” o “Descargar para Mac”


<div align="center"> 
  <img src="img/mac4.png" width="450">
</div>

- Abre la lista de archivos descargados de tu navegador, y encuentra el instalador
<div align="center"> 
  <img src="img/mac5.png" width="450">
</div>

- Arrastra el archivo Visual Studio Code.app a la carpeta Aplicaciones
<div align="center"> 
  <img src="img/mac6.png" width="450">
</div>

- Añade el editor al dock dándole click derecho al ícono que te aparece en pantalla y seleccionando “Options” u “Opciones”, y luego “Keep in dock” o “Mantener en el dock”

<div align="center"> 
  <img src="img/mac7.png" width="450">
</div>


#### Instalación de Python
El lenguaje de programación es la joya de la corona de nuestras herramientas. Sin Python no puedes programar, es así de simple. Sigue los siguientes pasos:

Abre tu navegador preferido (Safari, Chrome, el que quieras) y dirígete a

```python
https://www.python.org/downloads/
```
<div align="center"> 
  <img src="img/py1.png" width="450">
</div>

- Da click en el botón “Download Python 3.x.x”. En las “x” vas a ver números. Lo importante es que el primer número sea un 3, los dos que siguen no nos interesan, porque cambian todo el tiempo.

- Abre el instalador descargado, y sigue los pasos
<div align="center"> 
  <img src="img/py2.png" width="450">
</div>

<div align="center"> 
  <img src="img/py3.png" width="450">
</div>

## <a name="Instalación-de-nuestras-herramientas-en-Ubuntu">Instalación de nuestras herramientas en Ubuntu</a>


- La consola / terminal / línea de comandos
- El editor de código: Visual Studio Code
- El lenguaje de programación: Python

#### Instalación de la consola
En Ubuntu no necesitas instalar una consola a diferencia de Windows. Para poder usar la terminal debes presionar Ctrl + Alt + t y voilà, se abrirá frente a tus ojos

#### Instalación del editor de código
Abre tu navegador preferido (Firefox, Chrome, el que quieras) y dirígete a 

```python
https://go.microsoft.com/fwlink/?LinkID=760868
```
<div align="center"> 
  <img src="img/li0.png" width="450">
</div>

Abre el archivo descargado. Notarás que termina en “.deb”
<div align="center"> 
  <img src="img/li1.png" width="450">
</div>

Sigue los pasos de instalación

<div align="center"> 
  <img src="img/li2.png" width="450">
</div>

Introduce la contraseña de tu sistema:
<div align="center"> 
  <img src="img/li3.png" width="450">
</div>
Espera a que termine la instalación:
<div align="center"> 
  <img src="img/li4.png" width="450">
</div>
Instalación finalizada:

#### Instalación de Python
Abre tu terminal y ejecuta los siguientes comandos:

```python
sudo apt update
```
```python
sudo apt install python3-pip
```
Te mostrará si deseas continuar con la instalación, da click en enter.

La instalación empezará:

Ejecuta el comando para verificar que el lenguaje de programación se instaló correctamente

```python
python3 -V
```



```python
$ node app
```