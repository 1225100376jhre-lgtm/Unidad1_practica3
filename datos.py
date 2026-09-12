# Autor: <Tu nombre>
# Grupo: <Tu grupo>
# Inventario de Alumnos - Programacion de Redes
# Aqui van las funciones para leer y guardar el archivo de datos

import json

ARCHIVO_DATOS = "inventario.json"


def cargar_datos():
    # Intenta abrir el archivo, si no existe o esta vacio o mal escrito
    # regresa una lista vacia para que el programa no se cierre
    try:
        archivo = open(ARCHIVO_DATOS, "r", encoding="utf-8")
        contenido = archivo.read()
        archivo.close()

        if contenido.strip() == "":
            print("El archivo esta vacio, se inicia un inventario nuevo")
            return []

        datos = json.loads(contenido)
        return datos

    except FileNotFoundError:
        print("No existe el archivo, se creara uno nuevo al guardar")
        return []
    except json.JSONDecodeError:
        print("El archivo tiene un formato incorrecto, se inicia vacio")
        return []


def guardar_datos(inventario):
    # Guarda la lista de alumnos en el archivo json
    try:
        archivo = open(ARCHIVO_DATOS, "w", encoding="utf-8")
        json.dump(inventario, archivo, indent=4, ensure_ascii=False)
        archivo.close()
    except:
        print("Hubo un error al guardar el archivo")