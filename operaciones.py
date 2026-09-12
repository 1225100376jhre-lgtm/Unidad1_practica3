# operaciones.py
# Funciones del inventario de alumnos
# Cada alumno es un diccionario con: numero_control, nombre, apellidos, grupo, semestre

import time
from tabulate import tabulate


def mostrar_inventario(inventario):
    if len(inventario) == 0:
        print("El inventario esta vacio")
        return

    encabezados = ["No.Control", "Nombre", "Apellidos", "Grupo", "Cuatrimestre"]
    filas = []
    for alumno in inventario:
        fila = [alumno["numero_control"], alumno["nombre"], alumno["apellidos"], alumno["grupo"], alumno["cuatrimestre"]]
        filas.append(fila)

    print()
    print(tabulate(filas, headers=encabezados, tablefmt="grid"))
    print()


def agregar_elemento(inventario):
    print("\n-- Agregar alumno --")
    numero_control = input("Numero de control: ")

    if numero_control == "":
        print("El numero de control no puede estar vacio")
        return

    # revisamos que no exista ya ese numero de control
    for alumno in inventario:
        if alumno["numero_control"] == numero_control:
            print("Ya existe un alumno con ese numero de control")
            return

    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    grupo = input("Grupo: ")

    if nombre == "" or apellidos == "" or grupo == "":
        print("Nombre, apellidos y grupo son obligatorios")
        return

    try:
        cuatrimestre = int(input("Cuatrimestre: "))
    except ValueError:
        print("El cuatrimestre debe ser un numero")
        return

    alumno = {
        "numero_control": numero_control,
        "nombre": nombre,
        "apellidos": apellidos,
        "grupo": grupo,
        "cuatrimestre": cuatrimestre
    }

    inventario.append(alumno)
    print("Alumno agregado")
    time.sleep(1)


def buscar_elemento(inventario):
    if len(inventario) == 0:
        print("El inventario esta vacio")
        return

    dato = input("Buscar por numero de control o nombre: ").lower()
    encontrado = False

    for alumno in inventario:
        if dato in alumno["numero_control"].lower() or dato in alumno["nombre"].lower():
            print(alumno)
            encontrado = True

    if not encontrado:
        print("No se encontro ningun alumno")
    time.sleep(1)


def editar_elemento(inventario):
    if len(inventario) == 0:
        print("El inventario esta vacio")
        return

    numero_control = input("Numero de control del alumno a editar: ")

    for alumno in inventario:
        if alumno["numero_control"] == numero_control:
            try:
                nuevo_cuatrimestre = int(input("Nuevo cuatrimestre: "))
                alumno["cuatrimestre"] = nuevo_cuatrimestre
                print("Alumno actualizado")
                time.sleep(1)
            except ValueError:
                print("El cuatrimestre debe ser un numero entero")
            return

    print("No se encontro un alumno con ese numero de control")


def eliminar_elemento(inventario):
    if len(inventario) == 0:
        print("El inventario esta vacio")
        return

    numero_control = input("Numero de control del alumno a eliminar: ")

    for alumno in inventario:
        if alumno["numero_control"] == numero_control:
            inventario.remove(alumno)
            print("Alumno eliminado")
            time.sleep(1)
            return

    print("No se encontro un alumno con ese numero de control")