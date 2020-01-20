from libreria_script_musicos import *
import random


# VARIABLES GLOBALES: estas variables definen el nº de elementos a generar.
# Se han hecho pruebas generando menos datos para ver que todo funcionaba como debía,
# de ahí que se hayan separado de los métodos.

# Nº de grupos:
n_grupos = 200000
# Nº de conciertos:
n_conciertos = 100000
# Nº de discos:
n_discos = 1000000
# Nº de músicos:
n_musicos = 1000000

# Nº de canciones por disco:
canciones_por_disco_min = 10
canciones_por_disco_max = 14

# Nº de entradas por concierto (cantidad fijada. )
entradas_por_concierto = 240

# La mayoría de métodos generadores consisten en lo siguiente:
# Primero, se abre un archivo con un identificador asociado.
# Segundo, se inicializa una variable <contador> a 0, que será el código identificador de ese
# grupo de atributos.
# Tercero, se entra en un bucle generador de datos aleatorios y escritura en el archivo csv.
# Cuarto, se cierra el archivo de datos.

# El orden de ejecución de datos es el mismo que el orden de inserción en la BBDD, y es el mismo que el orden de los métodos siguientes.

# PRIMERO: generar script de grupos. Hay 200.000 grupos con 1.000.000 de músicos distribuidos en ellos.


def generar_grupos(rango):
    """ Dado un rango (nº de grupos a generar), genera en un archivo .csv
     ese nº de grupos, rellenando con datos aleatorios sus atributos. """

    # Identificador del archivo:
    grupos = open("grupos.csv", "w")

    # Esta lista contendrá los códigos de los grupos, usada para luego generar
    # el archivo de músicos, discos, etc.
    lista_codigos_grupos = []

    # Para cada grupo, genero sus atributos:
    for i in range(rango):
        # Código de grupo: realmente es un integer contador.
        codigo_grupo = i
        # Datos varios como nombre, genero, pais, etc.
        nombre_grupo = "".join(["grupo", str(i)])
        genero = random.choice(posibles_generos).strip()
        pais = random.choice(posibles_paises).strip()
        sitio_web = "".join(["www.", nombre_grupo, ".com"])

        # Cadena que se escribirá en el archivo:
        cadena = f"{codigo_grupo},{nombre_grupo},{genero},{pais},{sitio_web}\n"

        # Escribo el grupo en el archivo.
        grupos.write(cadena)

        # Añado a la lista el código del grupo.
        lista_codigos_grupos.append(codigo_grupo)
    # Cierro el identificador del archivo:
    grupos.close()
    return lista_codigos_grupos


# SEGUNDO: generar script de músicos asociados a los grupos. Distribuir entre 1 y 10 músicos por cada grupo.


def generar_musicos(lista_codigo_grupos):
    # Identificador del archivo:
    musicos = open("musicos.csv", "w")
    for i in range(n_musicos):
        # Código de músico: realmente es un integer contador.
        codigo_musico = i

        # Genero datos varios
        dni = genera_dni(i+1)
        nombre = "".join(["nombre", str(i)])
        direccion = "".join(["direccion", str(i)])
        codigo_postal = random.randint(10000, 99999)
        ciudad = "".join(["ciudad", str(i)])
        provincia = "".join(["provincia", str(i)])
        telefono = random.randint(900000000, 999999999)
        instrumentos = random.choice(posibles_instrumentos)
        codigo_grupo = random.choice(lista_codigo_grupos)
        # Cadena que se escribirá en el archivo:
        cadena = f"{codigo_musico},{dni},{nombre},{direccion},{codigo_postal},{ciudad},{provincia},{telefono},{instrumentos},{codigo_grupo}\n"
        musicos.write(cadena)
    musicos.close()

# TERCERO: generar Discos. Hay 1.000.000 de discos a distribuir entre 200.000 grupos. Media: 5 discos por grupo. Pongamos un rango de 3 a 7 discos / grupo.


def generar_discos(lista_codigo_grupos):
    contador_de_ids_de_discos = 0
    lista_de_codigos_disco = []
    discos = open("discos.csv", "w")

    for i in range(n_discos):
        codigo_disco = contador_de_ids_de_discos
        lista_de_codigos_disco.append(codigo_disco)
        contador_de_ids_de_discos += 1

        titulo = "".join(["disco", str(i)])
        fecha_edicion = fecha_aleatoria(
            "1/1/1980 1:30 PM", "1/1/2018 4:50 AM", random.random())
        genero = random.choice(posibles_generos).strip()
        formato = random.choice(posibles_formatos).strip()
        codigo_grupo_grupo = random.choice(lista_codigo_grupos)
        cadena = f"{codigo_disco},{titulo},{fecha_edicion},{genero},{formato},{codigo_grupo_grupo}\n"
        discos.write(cadena)
    discos.close()
    return lista_de_codigos_disco

# CUARTO: generar Canciones. Hay 12 canciones de media por disco. Pongamos un rango de 10 a 14 canciones por disco.


def generar_canciones(lista_de_codigos_disco):
    canciones = open("canciones.csv", "w")

    # Utilizo una variable contador externa debido a los dos bucles anidados.
    contador_de_ids_de_canciones = 0
    for codigo_disco in lista_de_codigos_disco:
        numero_canciones = random.randint(
            canciones_por_disco_min, canciones_por_disco_max)
        for i in range(numero_canciones):
            codigo = contador_de_ids_de_canciones
            contador_de_ids_de_canciones += 1
            nombre = "".join(["cancion", str(i)])
            compositor = "".join(["compositor", str(i)])
            fecha_grabacion = fecha_aleatoria(
                "1/1/1980 1:30 PM", "1/1/2018 4:50 AM", random.random())
            duracion = tiempo_aleatorio()
            codigo_disco_Discos = codigo_disco
            cadena = f"{codigo},{nombre},{compositor},{fecha_grabacion},{duracion},{codigo_disco_Discos}\n"
            canciones.write(cadena)
    canciones.close()

# QUINTO: generar conciertos. Hay 100000 conciertos en 20 paises, uno de ellos es Spain.


def generar_conciertos(numero_conciertos):
    conciertos = open("conciertos.csv", "w")
    lista_codigos_conciertos = []
    for i in range(numero_conciertos):
        codigo_concierto = i
        lista_codigos_conciertos.append(codigo_concierto)
        fecha_realizacion = fecha_aleatoria(
            "1/1/2016 1:30 PM", "1/1/2018 4:50 AM", random.random())
        pais = random.choice(posibles_paises).strip()
        ciudad = "".join(["ciudad", str(random.randint(0, 50)).strip()])
        recinto = "".join(["recinto", str(random.randint(0, 500)).strip()])
        cadena = f"{codigo_concierto},{fecha_realizacion},{pais},{ciudad},{recinto}\n"
        conciertos.write(cadena)
    conciertos.close()
    return lista_codigos_conciertos

# SEXTO: generar entradas para los conciertos. Hay 24 Millones de entradas distribuidas entre todos los conciertos.
# Habiendo 100000 conciertos, cada concierto tiene unas 240 entradas.


def generar_entradas(lista_codigos_conciertos):
    entradas = open("entradas.csv", "w")
    contador_entradas = 0
    for codigo_concierto in lista_codigos_conciertos:
        for i in range(entradas_por_concierto):
            codigo_entrada = contador_entradas
            contador_entradas += 1
            localidad = "".join(["ciudad", str(random.randint(0, 50)).strip()])
            precio = random.randint(20, 100)
            usuario = "".join(["usuario", str(i)])
            codigo_concierto_fk = codigo_concierto
            cadena = f"{codigo_entrada},{localidad},{precio},{usuario},{codigo_concierto_fk}\n"
            entradas.write(cadena)
    entradas.close()

# SÉPTIMO: tabla intermedia que asocia grupos con conciertos.
# Cada grupo ha tocado en al menos 10 conciertos y como mucho en 20
# La lista auxiliar se usa para no generar claves primarias duplicadas.


def generar_grupos_tocan_conciertos(lista_codigo_grupos, lista_codigos_conciertos):
    grupos_conciertos = open("grupos_tocan_conciertos.csv", "w")
    for codigo_grupo in lista_codigo_grupos:
        numero_conciertos = random.randint(10, 20)
        codigos_ya_usados = []
        for _ in range(numero_conciertos):
            codigo_concierto = random.choice(lista_codigos_conciertos)
            while(codigo_concierto in codigos_ya_usados):
                codigo_concierto = random.choice(lista_codigos_conciertos)
            codigos_ya_usados.append(codigo_concierto)
            cadena = f"{codigo_grupo},{codigo_concierto}\n"
            grupos_conciertos.write(cadena)
    grupos_conciertos.close()

# OCTAVO: Programa principal


def generar_archivos_csv():
    print("Generando grupos...")
    lista_codigos_grupos = generar_grupos(n_grupos)
    print("Generando musicos...")
    generar_musicos(lista_codigos_grupos)
    print("Generando discos...")
    lista_codigos_disco = generar_discos(lista_codigos_grupos)
    print("Generando canciones...")
    generar_canciones(lista_codigos_disco)
    print("Generando conciertos...")
    lista_conciertos = generar_conciertos(n_conciertos)
    print("Generando entradas...")
    generar_entradas(lista_conciertos)
    print("Generando grupos_tocan_conciertos...")
    generar_grupos_tocan_conciertos(lista_codigos_grupos, lista_conciertos)
    print("El script ha terminado.")


generar_archivos_csv()
