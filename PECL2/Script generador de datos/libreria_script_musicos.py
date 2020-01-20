"""
Librería de métodos y listas para generar el script de datos de músicos. . 
"""


import random
import time

# Librería de posibles generos musicales:
posibles_generos = ['clasica', ' blues', ' jazz', 'rock&roll', ' gospel', ' soul', ' rock',
                    ' metal', ' funk', ' disco', ' techno', ' pop', ' reggae', ' hiphop', 'salsa']

# Librería de posibles paises:
posibles_paises = ['Austria', ' Belgium', ' Croatia', ' Estonia', 'France', ' Germany', ' Greece', ' Hungary', ' Ireland', ' Italy',
                   ' Lithuania', ' Luxembourg', ' Malta', ' Netherlands', ' Poland', ' Portugal', ' Romania', ' Slovakia', ' Spain', ' Sweden']

# Librería de posibles formatos de disco:
posibles_formatos = ["CD", "Vinilo", "Digital"]

# Librería de posibles instrumentos:
posibles_instrumentos = ['Guitarra', 'Bajo', 'Bateria', 'Cantante', 'Violin', 'Piano', 'Flauta travesera colombiana',
                         'Laud medieval', 'Flauta', 'Trompeta', 'Trombon', 'Flauta de pan', 'Bongos', 'Triangulo']


def tiempo_aleatorio():
    """ Retorna una duración de canciones aleatoria entre 0 y 8 minutos y 0 a 60 segundos. """
    minutos = str(random.randint(0, 8)).zfill(2)
    segundos = str(random.randint(0, 59)).zfill(2)
    return "".join([minutos, ":", segundos])


def strTimeProp(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def fecha_aleatoria(start, end, prop):
    """ 
    Retorna una fecha aleatoria entre una mínima (start) y una máxima (end). 
    Ejemplo: fecha_aleatoria("1/1/1980 1:30 PM", "1/1/2018 4:50 AM", random.random())
    """

    cadena = strTimeProp(start, end, '%m/%d/%Y %I:%M %p', prop)
    cadena = cadena.split(" ")
    cadena = str(cadena[0])
    cadena = cadena.split("/")
    cadena = "".join([cadena[1], "-", cadena[0], "-", cadena[2]])
    return cadena

# Como no se pueden generar numeros aleatorios para el dni ya que podria haber duplicados, lo que hacemos
# es calcular cuantos 0s por la izquierda necesita el valor que entra para ser un dni valido


def genera_dni(numero_dni):
    """Como no se pueden generar numeros aleatorios para el dni ya que podria haber duplicados, lo que hacemos
    es calcular cuantos 0s por la izquierda necesita el valor que entra para ser un dni valido"""

    dni_aux = numero_dni
    dni_str = str(numero_dni)
    while(dni_aux < 10000000):
        dni_aux *= 10
        dni_str = "".join(["0", dni_str])

    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    valor = numero_dni % 23
    dni_final = dni_str + letras[valor]
    return dni_final
