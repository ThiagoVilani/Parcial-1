import json
import re

ruta = r"C:\Users\vilan\Desktop\test\pokedex.json"

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
    if re.search("minimo|maximo", clave, re.IGNORECASE):
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

def ordenar_poder(lista, clave):
    """
    """
    not_lista_ordenada = ""
    condicion = True
    while condicion:
        input_usuario = input("Desea ordenarlos de manera ascendente(asc) o descendente(desc)?\n>>>")
        if re.search("asc|desc", input_usuario, re.IGNORECASE):
            for i in range(len(lista)):
                minimo_maximo = encontrar_minimo_maximo(lista, clave, input_usuario)
                not_lista_ordenada = not_lista_ordenada + "{0}-{1}-{2}-{3}".format(i+1, lista[i]["nombre"], clave, lista[i][clave])
                lista.pop(i)
            condicion = False    
    return not_lista_ordenada

print(ordenar_poder(lista_pokemones, "poder"))