"""
Autor: Rosas Enriquez Jairo Haziel
Grupo: GTIR246
Inventario de Alumnos - Programacion de Redes

"""

import time
from datos import cargar_datos, guardar_datos
from operaciones import mostrar_inventario, agregar_elemento, buscar_elemento, editar_elemento, eliminar_elemento


def menu():
    #Imprime en pantalla las opciones del menu principal.
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
    """Funcion principal: carga los datos, muestra el menu y controla el flujo del programa."""
    # Cargamos el inventario guardado previamente 
    inventario = cargar_datos()

    # Bucle principal del programa, se repite hasta que el usuario elija salir
    while True:
        menu()
        opcion = input("Seleccione una opcion (1-6): ")

        # Segun la opcion elegida, llamamos a la funcion correspondiente
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
                # Antes de salir, guardamos los cambios hechos al inventario
                guardar_datos(inventario)
                print("Inventario guardado, saliendo del programa")
                break  # Rompemos el bucle para terminar el programa
            case _:
                # Si el usuario ingresa una opcion que no existe en el menu
                print("Opcion invalida, intente de nuevo")

        # Pausa breve antes de volver a mostrar el menu
        time.sleep(1)


if __name__ == "__main__":
    # Este bloque asegura que main() solo se ejecute si el archivo se corre directamente
    main()