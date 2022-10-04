import json
import re

ruta = r"C:\Users\vilan\Desktop\Programación & Laboratorio I\Parcial-1\test\pokedex.json"

def cargar_json(ruta:str):
    """
    Se encarga de cargar el archivo json\n
    Como parametro espera que ingrese la ruta del archivo en forma de string\n
    Retorna la lista contenida en el archivo
    """
    with open(ruta) as file:
        data = json.load(file)
    return data["pokemones"]
    
lista_pokemones = cargar_json(ruta).copy()

def listar_primeros_pokemones(lista:list):
    """
    Selecciona los primeros pokemones segun la cantidad elegida por el ususario\n
    Como parametro espera recibir la lista de los pokemones\n
    Retorna una string con formato de lista
    """
    condicion = True
    while condicion:
        input_usuario = input("Cuantos heroes desea listar?\nLa cantidad no puede ser mayor a {0}\n>>>".format(len(lista)))
        if re.search("r\D", input_usuario) == None:
            input_usuario = int(input_usuario)
            if input_usuario > 0 and input_usuario < len(lista):
                condicion = False
    not_lista_nombres = ""
    for i in range(input_usuario):
        not_lista_nombres = not_lista_nombres + "{0}-{1}\n".format(i+1, lista[i]["nombre"])
    return not_lista_nombres

def encontrar_minimo_maximo(lista:list, clave, min_max):
    """
    Se encarga de encontrar el valor minimo o maximo segun se requiera\n
    Como parametro espera recibir la lista de Pokemones, la clave del valor a comparar y la condicion a tomar(minimo o maximo)\n
    Retorna el la posicion del pokemon coincidente con lo deseado
    """
    minimo_maximo = 0
    if re.search("minimo|maximo", min_max, re.IGNORECASE):
        if min_max == "minimo":
            for i in range(len(lista)):
                if  lista[i][clave] < lista[minimo_maximo][clave]:
                    minimo_maximo = i
        else:
            for i in range(len(lista)):
                if  lista[minimo_maximo][clave] < lista[i][clave]:
                    minimo_maximo = i
    else:
        return -1    
    return minimo_maximo

def ordenar_por_valor(lista:list, clave:str):
    """
    Ordena una lista de manera creciente o decreciente segun el valor solicitado\n
    Como parmetro espera recibir la lista y la clave del valor\n
    Retorna una string con formato de lista
    """
    not_lista_ordenada = ""
    condicion = True
    while condicion:
        input_usuario = input("Desea ordenarlos de manera ascendente(asc) o descendente(desc)?\n>>>")
        if re.search("asc|desc", input_usuario, re.IGNORECASE):
            input_usuario = input_usuario.lower()
            if input_usuario == "asc":
                input_usuario = "minimo"
            else:
                input_usuario = "maximo"
            for i in range(len(lista)):
                minimo_maximo = encontrar_minimo_maximo(lista, clave, input_usuario)
                if minimo_maximo == -1:
                    return print("Error en los datos")
                not_lista_ordenada = not_lista_ordenada + "{0}-{1}  {2}-{3}\n".format(i+1, lista[minimo_maximo]["nombre"], clave, lista[minimo_maximo][clave])
                lista.pop(minimo_maximo)
            condicion = False    
    return not_lista_ordenada


def calcular_promedio(lista:list, clave:str):
    """
    Calcula el promedio de un cojunto de valores\n
    Compara todo los valores de la lista con el promedio y los lista segun superen o no el mismo\n
    Como parametros espera recibir la lista de pokemones y la clave del elemento a comparar\n
    Retorna una string con formato de lista de los elementos coincidentes con los parametros
    """
    condicion = True
    suma = 0
    lista_filtrada = ""
    for i in range(len(lista)):
        suma += len(lista[i][clave])

    promedio_key = suma/len(lista)
    while condicion:
        input_usuario = input("Desea conocer la lista de quienes tienen una cantidad mayor al promedio o quienes tienen una menor cantidad?\n-MAYOR\n-MENOR\n>>>")
        if re.search("mayor|menor", input_usuario, re.IGNORECASE):
            input_usuario = input_usuario.lower()
            condicion = False
            if input_usuario == "menor":
                lista_filtrada += "El promedio es de {0}. A continuacion se muestran los que se encuentran por debajo del mismo\n".format(promedio_key)
                for i in range(len(lista)):
                    if len(lista[i][clave]) < promedio_key:
                        lista_filtrada += "{0} / Cantidad: {1}\n".format(lista[i]["nombre"], len(lista[i][clave]))
            elif input_usuario == "mayor":
                lista_filtrada += "El promedio es de {0}. A continuacion se muestran los que se encuentran por encima del mismo\n".format(promedio_key)
                for i in range(len(lista)):
                    if len(lista[i][clave]) > promedio_key:
                        lista_filtrada += "{0} / Cantidad: {1}\n".format(lista[i]["nombre"], len(lista[i][clave]))
    return lista_filtrada


def crear_lista_tipos(lista:list):
    """
    Se encarga de imprimir la lista de todos los tipossd de pokemones\n
    Como parametro espera recibir la lista de los pokemones\n
    Retorna la lista de tipos
    """
    lista_tipos = []
    not_lista_tipos = ""
    for kokemon in range(len(lista)):
        for tipo in range(len(lista[kokemon]["tipo"])):
            lista_tipos.append(lista[kokemon]["tipo"][tipo])
    lista_tipos = set(lista_tipos)
    lista_tipos = list(lista_tipos)
    for tipo in range(len(lista_tipos)):
        not_lista_tipos += "{0}\n".format(lista_tipos[tipo].capitalize())
    return lista_tipos, not_lista_tipos


def buscar_listar_coincidencias(lista:list, not_lista, consigna_regex:str):
    """
    Busca todas las coincidencias entre el input del ususario 
    y los valores de la key "tipo".\n
    Como parametro espera recibir la lista de pokemones, 
    la lista de todos los tipos de pokemones existentes
    y la RegEx necesaria para hallar los valores.\n
    Retorna una string en formato de lista de todos los pokemones coincidentes
    """
    not_lista_tipos = "La lista de que Pokemon desea saber\n"
    not_lista_pokemones = ""
    while True:
        input_usuario = input(not_lista_tipos + not_lista)
        if re.search(consigna_regex, input_usuario, re.IGNORECASE) != None:
            input_usuario = input_usuario.lower()        
            for i in range(len(lista)):
                for tipo in lista[i]["tipo"]:
                    if re.search(input_usuario, tipo):
                        not_lista_pokemones += "{0} / Tipo/s: {1} \n".format(lista_pokemones[i]["nombre"], lista_pokemones[i]["tipo"])
            break
    return not_lista_pokemones


def Buscar_por_tipo(lista:list):
    """
    Se encarga de seleccionar los Pokemones coincidentes 
    con el tipo ingresado por el usuario y crear una lista\n
    Como parametro espera recibir la lista de los pokemones\n
    Retorna una string con formato de lista
    """
    lista_regex = ""
    lista_tipos, not_lista_tipos = crear_lista_tipos(lista)
    for i in range(len(lista_tipos)):
        lista_regex += "{0}|".format(lista_tipos[i])
    lista_regex = lista_regex.rstrip(lista_regex[-1])
    not_lista_pokemones_tipo = buscar_listar_coincidencias(lista, not_lista_tipos, lista_regex)
    return not_lista_pokemones_tipo



def exportar_csv(lista:str):
    """
    Se encargar de crear un archivo .csv y escribir en él lo que se ingrese\n
    El parametro esperado es el de una string \n
    No retorna nada\n
    """
    with open("Lista filtrada.csv", "w") as file:
        file.write(lista)

def menu():
    condicion = True
    while condicion:
        input_usuario = input("Que opcion desea elegir?\n1 - Listar los primeros Pokemones\n2 - Ordenarlos por el valor de poder\n3 - Ordenarlos por ID\n4 - Calcular la cantidad promedio por habilidad\n5 - Filtrar por tipo\n>>>")
        if re.search("[1-5]", input_usuario) != None:
            condicion = False
            if input_usuario == "1":
                lista_csv = listar_primeros_pokemones(lista_pokemones)
            else:
                if input_usuario == "2":
                    lista_csv = ordenar_por_valor(lista_pokemones, "poder")
                else:
                    if input_usuario == "3":
                        lista_csv = ordenar_por_valor(lista_pokemones, "id")
                    else:
                        if input_usuario == "4":
                            while True:
                                input_usuario = input("La cantidad promedio de cual cualidad desea saber?\n>>TIPO\n>>EVOLUCIONES\n>>FORTALEZA\n>>DEBILIDAD\n>>>")
                                if re.search("tipo|evoluciones|fortaleza|debilidad", input_usuario, re.IGNORECASE):
                                    input_usuario = input_usuario.lower()
                                    lista_csv = calcular_promedio(lista_pokemones, input_usuario)
                                    break
                        else:
                            lista_csv = Buscar_por_tipo(lista_pokemones)
    while True:
        input_usuario = input("Desea exportar la lista a un archivo .csv?\n>>SI\n>>NO\n>>>")
        if re.search("si|no", input_usuario, re.IGNORECASE):
            input_usuario = input_usuario.lower()
            if input_usuario == "si":
                exportar_csv(lista_csv)
            break
                        
    print(lista_csv)          



