"""
Autor: Rosas Enriquez Jairo Haziel
Grupo: GTIR246
Inventario de Alumnos - Programacion de Redes

"""
import json

ARCHIVO_DATOS = "inventario.json"  # Nombre del archivo donde se guarda/lee el inventario


def cargar_datos():
    """
    Carga el inventario desde el archivo JSON.
    Si el archivo no existe, esta vacio o tiene un formato incorrecto,
    regresa una lista vacia para que el programa pueda seguir funcionando.
    """
    try:
        archivo = open(ARCHIVO_DATOS, "r", encoding="utf-8")
        contenido = archivo.read()
        archivo.close()

        # Si el archivo existe pero no tiene contenido, iniciamos con lista vacia
        if contenido.strip() == "":
            print("El archivo esta vacio, se inicia un inventario nuevo")
            return []

        # Convertimos el contenido del archivo (texto JSON) a una lista/diccionario de Python
        datos = json.loads(contenido)
        return datos

    except FileNotFoundError:
        # Se ejecuta si el archivo no existe todavia
        print("No existe el archivo, se creara uno nuevo al guardar")
        return []
    except json.JSONDecodeError:
        # Se ejecuta si el contenido del archivo no es un JSON valido
        print("El archivo tiene un formato incorrecto, se inicia vacio")
        return []


def guardar_datos(inventario):
    """Guarda la lista de alumnos (inventario) en el archivo JSON."""
    try:
        archivo = open(ARCHIVO_DATOS, "w", encoding="utf-8")
        # indent=4 -> formatea el JSON con sangria para que sea legible
        # ensure_ascii=False -> permite guardar acentos y enies correctamente
        json.dump(inventario, archivo, indent=4, ensure_ascii=False)
        archivo.close()
    except:
        # Captura cualquier error inesperado al escribir el archivo
        print("Hubo un error al guardar el archivo")