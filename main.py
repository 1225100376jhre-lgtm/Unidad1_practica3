"""
Autor: Rosas Enriquez Jairo Haziel
Grupo: GTIR246
Inventario de Alumnos - Programacion de Redes

"""

import time
from datos import cargar_datos, guardar_datos
from operaciones import mostrar_inventario, agregar_elemento, buscar_elemento, editar_elemento, eliminar_elemento


def menu():
    print("--------------------------------")
    print("   INVENTARIO DE ALUMNOS")
    print("--------------------------------")
    print("1. Agregar Alumno")
    print("2. Mostrar Alumnos")
    print("3. Eliminar Alumno")
    print("4. Modificar Alumno")
    print("5. Buscar Alumno")
    print("6. Salir")
    print("--------------------------------")


def main():
    inventario = cargar_datos()

    while True:
        menu()
        opcion = input("Seleccione una opcion (1-6): ")

        match opcion:
            case "1":
                agregar_elemento(inventario)
            case "2":
                mostrar_inventario(inventario)
            case "3":
                eliminar_elemento(inventario)
            case "4":
                editar_elemento(inventario)
            case "5":
                buscar_elemento(inventario)
            case "6":
                guardar_datos(inventario)
                print("Inventario guardado, saliendo del programa")
                break
            case _:
                print("Opcion invalida, intente de nuevo")

        time.sleep(1)


if __name__ == "__main__":
    main()