from operator import pos
import re
import json

ruta = r"C:\Users\vilan\OneDrive\Escritorio\Programación & Laboratorio I\Parcial-1\PP_STARWARS\data.json"

def cargar_json(ruta:str):
    """
    Se encarga de cargar el archivo .json desde el exterior\n
    Como parametro espera recibir la ruta del archivo en formato string\n
    Retorna la lista contenida dentro del archivo
    """
    with open(ruta) as file:
        data = json.load(file)
    return data["results"]

lista_personajes = cargar_json(ruta).copy()


def encontrar_maximo(lista:list, clave:str, genero:str):
    """
    Se encargar de encontrar el valor maximo de una key\n
    Como parametro espera recibir la lista de los personajes, la key de la cual queremos saber el maximo y el genero en caso de que quisieramos discriminar por genero\n
    Retorna la posicion del diccionario que contiene al personaje con el valor maximo de la key en cuestion
    """ 
    maximo = 0
    #de aca
    if genero == "female":
        maximo = 4
    elif genero == "n/a":
        maximo = 1
    #hasta acà se que no deberia estar hardcodeado
    if genero != "None":
            for i in range(len(lista)):
                if (lista[i][clave]) > (lista[maximo][clave]) and lista[i]["gender"] == genero:
                    maximo = i
    else:
        for i in range(len(lista)):
            if int(lista[i][clave]) > int(lista[maximo][clave]):
                maximo = i
    
    return maximo 

def listar_altura_peso(lista:list, clave:str):
    """
    Se encarga de crear una lista ordenada de los personajes segun su altura o su peso\n
    Como parametro espera recibir la lista de los personajes y la key del valor que queramos usar para ordenar\n
    Retorna una string en formato de lista con los nombres de los personjes ya ordenados
    """
    if clave == "altura":
        not_lista_ordenada = "Personajes ordenados por altura de manera descendente\n"
        clavita = "Altura"
    else:
        not_lista_ordenada = "Personajes ordenados por peso de manera descendente\n"
        clavita = "Peso"
    for i in range(len(lista)):
        maximo = encontrar_maximo(lista, clave, "None")
        not_lista_ordenada += "{0} - {1}: {2}\n".format(lista[maximo]["name"], clavita, lista[maximo][clave])
        lista.pop(maximo)
    return not_lista_ordenada

def encontrar_mas_altos(lista:list):
    """
    Se encarga de encontrar los personajes mas altos de cada genero\n
    Como parametro espera recibir la lista de los personajes\n
    Retorna una string en formato de lista con los nombres y las alturas de cada uno de ellos
    """
    masculino_alto = encontrar_maximo(lista, "height", "male")
    femenino_alto = encontrar_maximo(lista, "height", "female")
    sin_genero_alto = encontrar_maximo(lista, "height", "n/a")
    lista_altos = "El masculino mas alto es {0}\nEl pesonaje femenino mas alto es {1}\nEl personaje sin genero mas alto es {2}".format(lista[masculino_alto]["name"], lista[femenino_alto]["name"], lista[sin_genero_alto]["name"])
    return lista_altos

def buscador_personajes(lista:list):
    """
    Se encarga de buscar y encontrar los personajes que quiera el usuario\n
    Como parametro espera recibir la lista de persnajes\n
    Retorna la posicion en la lista del personaje buscado
    """
    lista_regex = ""
    for i in range(len(lista)):
        lista_regex += "{0}|".format(lista[i]["name"])
        
    input_usuario = input("Ingrese el nombre del personaje que desea buscar")
    if re.search(lista_regex , input_usuario, re.IGNORECASE) != None:
        input_usuario = input_usuario.lower()
        for i in range(len(lista)):
            if re.search(input_usuario, lista[i]["name"]) != None:
                pos_personaje_buscado = i
    return pos_personaje_buscado

def exportar_archivo(lista_csv:str):
    with open("Personajes de Star Wars.csv", "w") as file:
        file.write()




