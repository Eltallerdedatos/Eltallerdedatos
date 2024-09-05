#!/usr/bin/env python
# coding: utf-8

# <img src="OriginalLogo.jpg" alt="El taller de datos" width="500"/>
# 

# 
# 
# #### Módulo 1: Python para la ciencia de datos
# 
# # 1. Introducción a Python. Lenguaje de programación y Sintaxis básica
# 
# #### Contenidos:
# * [Primeras instrucciones](#1)
# * [Variables](#2)
# * [Números](#3)
# * [Cadenas de texto (strings)](#4)
# * [Booleanos](#5)
# * [Prioridad de operaciones](#6)
# * [Estructuras alternativas IF-ELSE](#7)
# * [Estructuras repetitivas WHILE](#8)
# * [Estructuras repetitivas FOR](#9)
# * [Entrada-Salida estándar](#10)
# 
# 
# Python:
# 
# 📚 Lenguaje de programación: Ideal para principiantes y expertos.
# 
# 🎯 Propósito general: Usado en desarrollo web, ciencia de datos, automatización, y más.
# 
# 🔄 Multiparadigma: Soporta programación orientada a objetos, funcional, y procedimental.
# 
# ⚙️ Características principales:
# 
# 📜 Código limpio y legible: Sintaxis simple y clara.
# 
# 🚀 Tipado dinámico: No necesitas declarar tipos de datos.
# 
# 🔄 Interpretado: Ejecuta el código línea por línea sin necesidad de compilar.
# 
# 💻 Multiplataforma: Funciona en Windows, macOS y Linux.
# 
# ## 🧠 Ventajas:
# 
# ⌛ Ahorra tiempo: Menos líneas de código para tareas complejas.
# 
# 🌍 Gran comunidad: Amplia documentación, bibliotecas y soporte.
# 
# 🛠️ Gestión automática de memoria: Facilita la programación y reduce errores.
# 
# 🚧 Consideraciones:
# 
# 🐢 Puede ser más lento que lenguajes compilados como C o Java.
# 
# 🎢 Curva de aprendizaje: Inicialmente puede ser abrumador debido a la cantidad de herramientas disponibles.
# 
# 
# 
# ## 1.1 Primeras instrucciones <a class="anchor" id="1"></a>
# 
# Vamos a comenzar con las instrucciones más básicas que podemos usar en Python
# 
# 
# 
# ## 1.1 Primeras instrucciones <a class="anchor" id="1"></a>
# 
# Vamos a comenzar con las instrucciones más básicas que podemos usar en Python

# # Ejercicio 1: Imprimir un Mensaje en la Consola
# 
# Objetivo: Aprender a usar la función print() para mostrar mensajes en la consola.
# 
# Instrucción: Escribe un programa que imprima "¡Hola, mundo!" en la consola.

# In[1]:


print("¡Hola, mundo!")


# # Ejercicio 2: Uso de la Función help()
# 
# Objetivo: Familiarizarte con la documentación de Python directamente en la consola.
# Instrucción: Usa la función help() para obtener información sobre cualquier función o módulo de Python.

# In[2]:


help('print')


# ## 1.2 Variables <a class="anchor" id="2"></a>
# 
# En programación, las variables son contenedores que almacenan datos, y el tipo de variable determina el tipo de datos que se pueden almacenar en ellas. En Python (y otros lenguajes de programación), existen varios tipos de variables que definen el tipo de datos que pueden almacenar. Aquí te explico los principales tipos de variables en Python:
# 
# 🔢 Flotantes (float): Guardan números decimales o fraccionarios.
# 
# 📝 Cadenas de texto (str): Contienen secuencias de caracteres, como palabras o frases.
# 
# ✅ ❌ Booleanos (bool): Almacenan valores de verdadero o falso.
# 
# 📋 Listas (list): Son colecciones de elementos ordenados que pueden contener cualquier tipo de dato.
# 
# 📦 Tuplas (tuple): Similares a las listas, pero inmutables (no se pueden modificar después de ser creadas).
# 
# 🎲 Conjuntos (set): Almacenan elementos únicos, sin duplicados, en una colección no ordenada.
# 
# 🔑📄 Diccionarios (dict): Guardan pares clave-valor, donde cada valor está asociado a una clave única.
# 
# ❓ NoneType: Representa la ausencia de valor o la falta de asignación de un valor.
# 
# En Python, al ser de tipado dinámico, el tipo de variable se asigna automáticamente según el valor dado.

# # Ejercicio 3: Crear tu Primera Variable
# Objetivo: Aprender a definir y usar variables.
# Instrucción:
# Define una variable llamada nombre que almacene tu nombre y luego imprímelo con un mensaje personalizado.

# In[10]:


nombre = "Silvia"
print("Hola, " + nombre + "!")


# In[3]:


x = 5


# In[4]:


type(x)


# In[5]:


x = 5.0


# In[6]:


type(x)


# In[7]:


print(x)


# In[8]:


print(y)


# Una vez que hemos visto cómo asignar valor a una variable, vamos a hacer un repaso de los tipos más básicos que podemos utilizar en Python
# 
# ## 1.3 Números <a class="anchor" id="3"></a>
# 
# Vamos a comenzar a probar Python como una gran calculadora

# In[ ]:


2+2


# In[ ]:


8-2*2


# In[ ]:


(8-2)*2


# In[ ]:


8//5


# In[ ]:


8/5


# In[ ]:


11%2


# In[ ]:


5**2


# Python tiene incluidos varios tipos de datos numéricos. Los tipos básicos son int (enteros), float (reales) y complex (complejos).
# 
# Números enteros:
# - los definimos sin incluir decimales
# - la aritmética de números enteros es muy potente en Python y no tiene límites (excepto el de la memoria). 

# In[ ]:


5


# In[ ]:


2**689-1


# Los números reales se definen mediante el uso de decimales.

# In[ ]:


5.0


# In[ ]:


1.0+2*10**-16


# Los números complejos se definen mediante una parte real y una parte imaginaria utilizando la letra j

# In[ ]:


5+1j


# En cualquier caso, podemos conocer el tipo mediante la instrucción type

# In[ ]:


type(1)


# In[ ]:


type(1.0)


# In[ ]:


type(1+0j)


# Además, podemos operar con números de distintos tipos, en cuyo caso el resultado será el tipo más general que aparezca en la operación

# In[ ]:


type(2+3)


# In[ ]:


type(2+3.0)


# In[ ]:


type(2+(3+0j))


# Podemos también transformar números de un tipo a otro utilizando el nombre del tipo a modo de función

# In[ ]:


int(5.4)


# In[ ]:


float(3)


# In[ ]:


complex(2.5)


# Para más información y otras funciones: 
# 
# ## 1.4 Cadenas de texto (strings) <a class="anchor" id="4"></a>
# 
# El tipo string lo forman una cadena de caracteres encerrada entre comillas dobles o apóstrofes

# In[ ]:


'Hola mundo'


# In[ ]:


"Hola mundo"


# In[ ]:


type('Hola mundo')


# In[ ]:


type("Hola mundo")


# Podemos incluir (sin necesidad de usar caracteres especiales) las dobles comillas o los apóstrofes dentro del propio string

# In[ ]:


'Hola "mundo" hola'


# In[ ]:


"Hola 'mundo' hola"


# E incluso podemos utilizar las triples comillas para introducir saltos de línea.

# In[ ]:


print("""Hola
mundo""")


# In[ ]:


print('''Hola
mundo''')


# En realidad, lo que estamos haciendo es introducir el caracter especial \n como salto de línea dentro del string

# In[ ]:


"""Hola
mundo"""


# De la misma manera, podríamos haberlo introducido manualmente el caracter \n o cualquier otro caracter especial.

# In[ ]:


print("Hola\nmundo")


# print("Hola\tmundo")

# In[ ]:


print("Hola\\mundo")


# El tipo string permite realizar un acceso individualizado a cada caracter

# In[ ]:


s = "Python"


# In[ ]:


s[0]


# In[ ]:


s[1]


# In[ ]:


s[2]


# In[ ]:


s[3]


# In[ ]:


s[4]


# In[ ]:


s[5]


# De la misma manera que con los números, podemos "operar" entre strings. Verás que hay varios operadores que tienen diferentes acciones en función del tipo de variable con el que operan. Ejemplos son los operadores sobrecargados + y *.

# In[ ]:


'Hola' + ' Mundo'


# In[ ]:


'Hola Mundo ' * 3


# Y también podemos transformar varibales de tipo numérico a string, y viceversa.

# In[ ]:


str(5)


# In[ ]:


str(4.3)


# Python disponen de multitud de funciones built-in que permiten manejar los strings de manera muy cómoda (https://docs.python.org/3.7/library/stdtypes.html#string-methods). Estas funciones nos permiten pasar los strings a mayúsculas, minúsculas, contar el número de caracteres, encontrar la posición de un determinado caracter, etc. Una de las más básicas es la función `len`.

# In[ ]:


len('Hola')


# ## 1.5 Booleanos <a class="anchor" id="5"></a>
# 
# El último tipo que vamos a ver en esta introducción es el tipo Booleano (verdadero o falos), representados por los valores True y False

# In[ ]:


a = True


# In[ ]:


type(a)


# In[ ]:


b = False


# In[ ]:


type(b)


# En realidad, en Python cualquier variable "nula" tiene el caracter False (el 0, el 0.0,...). Cualquier otro valor es considerado True. Esto podemos verlo fácilmente mediante la función bool que nos permite transformar una variable a tipo booleano.

# In[ ]:


a = 0.0
bool(a)


# In[ ]:


a = 5
bool(a)


# El tipo de variable boolenaa tiene asociados varios operadores, tanto unarios como binarios (de comparación). Los más utilizados son:
# * `>`: Mayor 
# * `<`: Menor 
# * `>=`: Mayor o igual 
# + `<=`: Menor o igual
# * `==` igualdad
# * `and`: conjunción
# * `or`: disyunción
# * `not`: negación

# In[ ]:


5 > 4


# In[ ]:


(5<=3) and (4>2)


# In[ ]:


2-2==1/2


# In[ ]:


2-2==1//2


# ## 1.6 Prioridad de operaciones <a class="anchor" id="6"></a>
# 
# Al igual que en otros lenguajes de programación, podemos añadir consecutivamente varias operaciones, debiendo tener en cuenta las prioridades que existen entre operadores. Ante la duda, la separación de expresiones excesivamente largas en varias etapas puede ser una buena alternativa. En cualquier caso, el orden de mayor a menor prioridad es:
# * Paréntesis
# * Exponentes
# * Multiplicación y división
# * Sumas y restas
# * Operadores lógicos
# 
# Cuando en una secuencia hay varios operadores de la misma prioridad, la ejecución será siempre de izquierda a derecha

# In[ ]:


5-2**2


# In[ ]:


5-2-1


# In[ ]:


True or True and False


# ## 1.7 Estructuras alternativas IF-ELSE <a class="anchor" id="7"></a>
# 
# La estructura alternativa IF-ELSE se utiliza en Python de la siguiente manera:
# 
# python
# Copiar código
# if condicion:
#     instruccion o lista de instrucciones
# Los puntos clave a tener en cuenta sobre la sintaxis en Python son los siguientes:
# 
# Debemos colocar dos puntos (:) justo después de la condición.
# Todas las instrucciones que forman parte del bloque IF deben estar indentadas. La indentación es lo que permite agrupar una secuencia de instrucciones dentro de una estructura de control, similar al uso de begin-end o {} en otros lenguajes.
# 

# In[ ]:


if condicion:
    instruccion o lista de instrucciones


# In[ ]:


a = 6
if a > 5:
    print('la variable es mayor que 5')


# Si queremos introducir un bloque ELSE, escribiremos:
# 
# `if condicion:
#     instruccion o lista de instrucciones
#  else:
#     instruccion o lista de instrucciones`

# In[ ]:


a = 6
if a > 5:
    print('la variable es mayor que 5')
else:
    print('la variable no es mayor que 5')


# Podemos seguir anidando más bloques alternativos dentro de otros

# In[ ]:


a = 5
if a > 5:
    print('la variable es mayor que 5')
else:
    if a < 5:
        print('la variable es menor que 5')
    else:
        print('la variable es igual a 5')


# Sin embargo, cuando tenemos varias condiciones sobre el mismo conjunto de variables, podemos utilizar la contracción `elif` para ir secuenciando las condiciones.

# In[ ]:


a = 4
if a > 5:
    print('la variable es mayor que 5')
elif a < 5:
    print('la variable es menor que 5')
else:
    print('la variable es igual a 5')


# ## 1.8 Estructuras repetitivas WHILE <a class="anchor" id="8"></a>
# 
# a estructura WHILE nos permite repetir una secuencia de instrucciones mientras se cumpla una condición. La sintaxis es muy similar a la de la estructura IF, y se escribe de la siguiente manera:
# 
# 
#     instrucción o lista de instrucciones
# Durante la ejecución, las instrucciones dentro del bloque while se seguirán repitiendo hasta que la condición deje de ser verdadera. Al igual que en otras estructuras, es importante recordar que las instrucciones dentro del bloque deben estar indentadas para pertenecer al ciclo while.

# In[ ]:


while condicion:
    instrucción o lista de instrucciones


# In[ ]:


x = 5
while x >= 0:
    print (x)
    x = x-1


# La instrucción `break` nos permite romper la ejecución del while sin atender a la condición

# In[ ]:


x = 9
y = 0
while x >= 0:
    print(x)
    x = x - 1
    y = y + 2
    if x == y:
        print('Las variables tienen el mismo valor')
        break
    


# Aunque a veces no tenga demasiada utilizada, las estructuras while disponen también de una instrucción `else`, que se ejecutará únicamente cuando la condición del while se evalúe a `False`

# In[ ]:


x = 9
y = 1
while x >= 0:
    print(x)
    x = x - 1
    y = y + 2
    if x == y:
        print('Las variables tienen el mismo valor')
        break
else:
    print('Las variables nunca han alcanzado el mismo valor')


# ## 1.9 Estructuras repetitivas FOR <a class="anchor" id="9"></a>
# 
# Cuando la repetición de una secuencia de instrucciones no depende de una condición, podemos utilizar la estructura FOR de la siguiente manera:
# 
# `for variable in elemento_iterable:
#     instrucción o secuencia de instrucciones`
#     
# El concepto de elemento iterable (lo veremos con más profunidad en el siguiente tema) debe ser una variable (explícita o no) que contenga un conjunto de elementos por los que ir iterando. Veámoslo con un ejemplo:

# In[ ]:


for x in [5, 7 ,-1]:
    print(x)


# En el ejemplo anterior, el conjunto iterable es una lista de elementos. La estructura for va iterando sobre dicha lista, asignando a la variable x cada uno de los elementos que aparecen en la lista.

# In[ ]:


for palabra in ['Hola', 'que', 'tal']:
    print(palabra)


# Incluso los propios `strings` pueden considerarse como elementos iterables, pudiendo fácilmente hacer un recorrido por sus caracteres.

# In[ ]:


for letra in 'Experto':
    print(letra)


# Sin embargo, la mayoría de las veces queremos utilizar la estructura FOR para ejecutar un número concreto de iteraciones (por ejemplo, 10). En este caso, podríamos hacer lo siguiente...

# In[ ]:


for i in [0,1,2,3,4,5,6,7,8,9]:
    print(i)


# ...Pero no tiene mucho sentido cuando el número de ejecuciones sea mucho más grande (100, 1000). Para ello, podemos utilizar la función `range`, que nos devuelve un elemento iterable (lista) con los números que especifiquemos. Por ejemplo, `range(10)` nos devolverá un iterables como el del ejemplo anterior.

# In[ ]:


for i in range(10):
    print(i)


# La función `range` posee además otros parámetros optativos que nos permiten mayor flexibilidad en los elementos iterables.

# In[ ]:


for i in range(5, 10):
    print(i)


# In[ ]:


for i in range(0, 10, 3):
    print(i)


# Al igual que ocurre en la estructura WHILE, podemos romper la ejecución del FOR antes de "agotar" el elemento iterable mediante la instrucción `break`. También disponemos de una instrucción `else` que se ejecutará como última instrucción una vez agotado el elemento iterable.

# ## 1.10 Entrada-salida estándar <a class="anchor" id="10"></a>
# 
# Por último, vamos a ver cómo leer/escribir información desde y hacia el exterior a través del teclado y la pantalla, lo cual será útil para estas primeras semanas de entrenamiento.
# 
# La entrada de datos por teclado la realizaremos mediante la instrucción `input`, que nos devolverá un string recogido del teclado.

# In[ ]:


x = input('Introduce algo: ')
print(x)


# Es importante recordar que la entrada siempre es de tipo string y, por tanto, debemos transformar las variables al tipo necesario antes de poder operar con ellas.

# In[ ]:


x = input('Introduce un numero: ')
x = x + 1
print(x)


# In[ ]:


x = int(input('Introduce un numero: '))
x = x + 1
print(x)


# La salida de datos por pantalla la haremos mediante la instrucción `print`. El print nos permite concatenar sucesivas variables o literales.

# In[ ]:


print('hola', ' que', ' tal')


# In[ ]:


print('El numero es ', 5)


# In[ ]:


x = 5
print('El numero es ', x)


# In[ ]:


x = 5
print('El numero es ', x, ' y el siguiente es ', x+1)


# De una manera muy parecida a C, podemos utilizar caracteres especiales para el formato del string, utilizando `%d` (para enteros), `%f` (para reales), etc...

# In[ ]:


x = 4
l = 3.14 * 2 * x
print('La longitud de la circunferencia es %f' % l)


# Otra forma más simple de poder combinar variables y literales es la utilización del método `format`. Lo que hacemos con este método es "formatear" un string supliendo los huecos con valores de variables.

# In[ ]:


print("Numeros {} y {}".format(1, 3))


# In[ ]:


x = 4
print('La longitud de la circunferencia es {}'.format(2*3.14159*x))


# In[ ]:


x = 4
print('La longitud de la circunferencia es {:.2f}'.format(2*3.14159*x))


# Podemos incluso numerar los huecos

# In[ ]:


print("Hola {0} y {1}".format('Pepe', 'Antonio'))


# In[ ]:


print("Hola {1} y {0}".format('Pepe', 'Antonio'))


# In[ ]:


print("Hola {0}, {1}, {1} y {0}".format('Pepe', 'Antonio'))


# In[ ]:




