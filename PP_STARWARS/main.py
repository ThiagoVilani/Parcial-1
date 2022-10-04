'''
1 - Listar los personajes ordenados por altura
2 - Mostrar el personaje mas alto de cada genero
3 - 3 - Ordenar los personajes por peso
4 - Armar un buscador de personajes 
5 - Exportar lista personajes a CSV
6 - Salir

'''
import funciones
from funciones import lista_personajes
def starwars_app():
        print("1 - Listar los personajes ordenados por altura\n2 - Mostrar el personaje mas alto de cada genero\n3 - Ordenar los personajes por peso\n4 - Armar un buscador de personajes\n5 - Exportar lista personajes a CSV\n6 - Salir\n")
        respuesta = input("Ingrese el numero de la opcion escogida")
        if(respuesta=="1"):
            print("1 - Listar los personajes ordenados por altura\n")
            print(funciones.listar_altura_peso(lista_personajes, "height"))
        elif(respuesta=="2"):
            print("2 - Mostrar el personaje mas alto de cada genero\n")
            print(funciones.encontrar_mas_altos(lista_personajes))
        elif(respuesta=="3"):
            print("3 - Ordenar los personajes por peso\n")
            print(funciones.listar_altura_peso(lista_personajes, "mass"))
        elif(respuesta=="4"):
            print("4 - Armar un buscador de personajes\n")
            pos = funciones.buscador_personajes(lista_personajes)
            print(lista_personajes[pos])
        elif(respuesta=="5"):
            print("5 - Exportar lista personajes a CSV\n")
        elif(respuesta=="6"):
           pass

starwars_app()

