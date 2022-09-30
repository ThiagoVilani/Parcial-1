import re
import json


data_stark_json = r"C:\Users\vilan\OneDrive\Escritorio\Programación & Laboratorio I\Parcial-1\Clase 10\data_stark .json"

#--------------------------------------------------------------------
def Mensaje_error_datos():
    print("Hay un error en los datos, reviselo")
#--------------------------------------------------------------------


#--------------------------------------------------------------------
def Copiar_archivo(nombre_archivo:str):
    """
    Abre el archivo .json y crea una copia del mismo para trabjar sobre ella\n
    El parametro esperado es la ruta del archivo\n
    Retorna una copia del archivo .json
    """
    with open(nombre_archivo) as archivo:
        data = json.load(archivo)
        dic_heroes = data.copy()
    return dic_heroes
#--------------------------------------------------------------------

dic_heroes = Copiar_archivo(data_stark_json)


#--------------------------------------------------------------------
def Validar_input_usuario(lista_heroes:list):
    """
    Valida que el input ingresado sea uno o mas numeros del 0 al 9\n
    Valida que el numero ingresado no sea mayor a la cantidad de heroes\n
    El parametro esperado es la lista de heroes\n
    Retorna el input del usuario, ya habiendola verificado
    """
    input_usuario = input("Ingrese la cantidad de heroes que quiere ver listados. No puede ser mayor a {0}".format(len(lista_heroes)))
    if re.search("[0-9]+", input_usuario) == None:
        return Mensaje_error_datos()
    else:
        input_usuario = int(input_usuario)
        if input_usuario > len(lista_heroes) or input_usuario < 1:
            return Mensaje_error_datos()
    return input_usuario
#--------------------------------------------------------------------


#--------------------------------------------------------------------
def Listar_n_heroes(cant_heroes:int, lista_heroes:list):
    """
    Crea una lista de los nombres de los primeros N heroes\n
    Los parametros esperados son la cantidad de heroes y la lista de heroes\n
    Retorna la lista creada en forma de string
    """
    lista_primeros_heroes = ""
    for i in range(cant_heroes):
        astring = "{0}\n".format(lista_heroes[i]["nombre"])
        lista_primeros_heroes = lista_primeros_heroes + astring
        print(lista_heroes[i]["nombre"])
    return lista_primeros_heroes
#--------------------------------------------------------------------

#/|/|/|/|/|ORDENAMOS ALTURA/|/|/|/|/|/|
#--------------------------------------------------------------------
def Validar_input_orden():
    """
    Pregunta al usuario en que orden desea crear la lista\n
    Valida que el input ingresado sea asc o desc\n
    Retorna el input ya verificado
    """
    input_usuario = input("Desea ordenar la lista de manera ascendente(asc) o descendente(desc)?")
    if re.search("asc|desc", input_usuario, re.IGNORECASE) == None:
        return Mensaje_error_datos()
    else:
        input_usuario = input_usuario.lower()
        return input_usuario


def Buscar_minimo_maximo_altura(min_max:str, lista:list):
    """
    Encuentra el valor minimo o maximo de una lista\n
    Espera que los parametros sean: la palabra minimo o maximo segun la decision del usuario\n
    El segundo parametro esperado es una lista
    """
    minimo_maximo = 0
    for i in range(len(lista)):
        if min_max == "asc":
            if lista[i]["altura"] < lista[minimo_maximo]["altura"]:
                minimo_maximo = i
        elif min_max == "desc":
            if lista[i]["altura"] > lista[minimo_maximo]["altura"]:
                minimo_maximo = i
    return minimo_maximo


def Ordenar_listar_heroes_altura(lista:list):
    """
    Tomando el valor retornado por la funcion minimo-maximo,\n
    ordena la lista de la manera deseada\n
    Espera que el parametro ingresado sea la lista de heroes\n
    Retorna la lista ordenada en forma de string
    """
    input_usuario = Validar_input_orden()
    lista_ordenada = ""
    for i in range(len(lista)):
        minimo_maximo = Buscar_minimo_maximo_altura(input_usuario, lista)
        astring = "Nombre: {0}  Altura: {1}\n".format(lista[minimo_maximo]["nombre"], lista[minimo_maximo]["altura"])
        lista_ordenada = lista_ordenada + astring
        lista.pop(minimo_maximo)
    return lista_ordenada
#--------------------------------------------------------------------

#/|/|/|/|/|ORDENAMOS FUERZA/|/|/|/|/|/|
#--------------------------------------------------------------------
def Buscar_minimo_maximo_fuerza(min_max:str, lista:list):
    """
    Encuentra el valor minimo o maximo de una lista\n
    Espera que los parametros sean: la palabra minimo o maximo segun la decision del usuario\n
    El segundo parametro esperado es una lista
    """
    minimo_maximo = 0
    for i in range(len(lista)):
        if min_max == "asc":
            if lista[i]["fuerza"] < lista[minimo_maximo]["fuerza"]:
                minimo_maximo = i
        elif min_max == "desc":
            if lista[i]["fuerza"] > lista[minimo_maximo]["fuerza"]:
                minimo_maximo = i
    return minimo_maximo


def Ordenar_listar_heroes_fuerza(lista:list):
    """
    Tomando el valor retornado por la funcion minimo-maximo,\n
    ordena la lista de la manera deseada\n
    Espera que el parametro ingresado sea la lista de heroes\n
    Retorna la lista ordenada en forma de string
    """
    input_usuario = Validar_input_orden()
    lista_ordenada = ""
    for i in range(len(lista)):
        minimo_maximo = Buscar_minimo_maximo_fuerza(input_usuario, lista)
        astring = "Nombre: {0}  Fuerza: {1}\n".format(lista[minimo_maximo]["nombre"], lista[minimo_maximo]["fuerza"])
        lista_ordenada = lista_ordenada + astring
        lista.pop(minimo_maximo)
    return lista_ordenada
#--------------------------------------------------------------------


#--------------------------------------------------------------------
def Calcular_promedio(lista:list):
    """
    Calcula el promedio del tipo de valor que se requiera\n
    Segun la eleccion del usuario crea una lista con los heroes que superen o no el promedio\n
    El parametro esperado es la lista de heroes\n
    Retorna la lista creada en forma de string
    """
    clave = input("""De cual parametro desea calcular el promedio? 
                ALTURA
                FUERZA
                PESO""")
    mayor_menor = input("""Quiere filtrar a los que superen el promedio o a los que queden por debajo del mismo?
                        -MAYOR
                        -MENOR""")
    if re.search("peso|fuerza|altura", clave, re.IGNORECASE) == None:
        return Mensaje_error_datos()
    if re.search("mayor|menor", mayor_menor, re.IGNORECASE) == None:
        return Mensaje_error_datos()
    
    lista_filtrada = ""
    mayor_menor = mayor_menor.lower()
    clave = clave.lower()
    suma = 0
    for i in range(len(lista)):
        suma += lista[i][clave]
    promedio = suma/len(lista)
    if mayor_menor == "mayor":
        lista_filtrada = lista_filtrada + "El promedio es de {0}\nLos siguientes heroes son los que estan por encima del mismo\n".format(promedio)
        for i in range(len(lista)):
            if lista[i][clave] > promedio:
                astring = "Nombre: {0} {1}: {2}\n".format(lista[i]["nombre"], clave, lista[i][clave])
                lista_filtrada = lista_filtrada + astring
    elif mayor_menor == "menor":
        lista_filtrada = lista_filtrada + "El promedio es de {0}\nLos siguientes heroes son los que estan por debajo del mismo\n".format(promedio)
        for i in range(len(lista)):
            if lista[i][clave] < promedio:
                astring = "Nombre: {0} {1}: {2}\n".format(lista[i]["nombre"], clave, lista[i][clave])
                lista_filtrada = lista_filtrada + astring
    return lista_filtrada
#--------------------------------------------------------------------


#--------------------------------------------------------------------
def Filtrar_inteligencia(lista:list):
    """
    Mediante el input decide por cual valor de 'inteligencia' debe filtrar\n
    y crea una nueva lista con los nombres de los heroes\n
    El parametro esperado es la lista de heroes\n
    Retorna la lista filtrada y ordenada en forma de string
    """
    inteligencia = input("""Los heroes de cual tipo de inteligencia desea saber?
                        >GOOD
                        >AVERAGE
                        >HIGH""")
    if re.search("good|average|high", inteligencia, re.IGNORECASE) == None:
        return Mensaje_error_datos()

    lista_inteligentes = ""
    inteligencia = inteligencia.lower()
    for i in range(len(lista)):
        if inteligencia == lista[i]["inteligencia"]:
            astring = "Nombre: {0} Inteligenica: {1}\n".format(lista[i]["nombre"], lista[i]["inteligencia"])
            lista_inteligentes = lista_inteligentes + astring
    return lista_inteligentes
#--------------------------------------------------------------------


#--------------------------------------------------------------------
def Exportar_csv(lista:list):
    """
    Se encargar de crear un archivo .csv y escribir en él lo que se ingrese\n
    El parametro esperado es el de una string \n
    No retorna nada\n
    """
    with open("Lista Ordenada.csv", "w") as file:
            file.write(lista)
#--------------------------------------------------------------------


#--------------------------------------------------------------------
def Menu():
    """
    Se encarga de mostrarle las opciones al usuario y segun la eleccion\n
    y redirigirlo a la funcion correspondiente para suplir la demanda\n
    No espera ningun parametro\n
    No retorna nada
    """
    input_usuario = input(
    """
    Que opcion desea elegir?
    1->>Filtrar los primeros heroes
    2->>Ordenar los heroes por altura
    3->>Ordenar los heroes por fuerza
    4->>Calcular el promedio y filtrar los que superen o no el mismpo
    5->>Filtrar los heroes segun su inteligencia\n
    >>>""")

    if re.search("[1-5]", input_usuario) == None:
        return Mensaje_error_datos()
    if input_usuario == "1":
        input_usuario = Validar_input_usuario(dic_heroes["heroes"])
        lista_lista = Listar_n_heroes(input_usuario, dic_heroes["heroes"])
    else:
        if input_usuario == "2":
            lista_lista = Ordenar_listar_heroes_altura(dic_heroes["heroes"])
        else:
            if input_usuario == "3":
                lista_lista = Ordenar_listar_heroes_fuerza(dic_heroes["heroes"])
            else:
                if input_usuario == "4":
                    lista_lista = Calcular_promedio(dic_heroes["heroes"])
                else:
                    if input_usuario == "5":
                        lista_lista = Filtrar_inteligencia(dic_heroes["heroes"])
    eleccion_imprimir = input("""Desea guardar la lista en un archivo .csv?
                        >SI
                        >NO""")
    if re.search("si|no", eleccion_imprimir, re.IGNORECASE) == None:
        return Mensaje_error_datos()
    eleccion_imprimir = eleccion_imprimir.lower()
    if eleccion_imprimir == "si":
        print(lista_lista)
        Exportar_csv(lista_lista)
    else:
        print(lista_lista)
#--------------------------------------------------------------------


# listita = Filtrar_inteligencia(dic_heroes["heroes"])
#
# for i in range(len(listita)):
#    print(listita[i]["nombre"], listita[i]["inteligencia"])


