import json

ruta = r"C:\Users\vilan\Desktop\Programación & Laboratorio I\Parcial-1\Practica Paulina\data_paulina.json"

def cargar_archivo(ruta_archivo:str):
    """
    Se encarga de traer un archivo exterior y guardarlo en una variable\n
    Como parametro espera la ruta del archivo en formato string\n
    Retorna una copia del archivo cargado
    """
    with open(ruta_archivo) as file:
        data = json.load(file)
        print(data)

cargar_archivo(ruta)


