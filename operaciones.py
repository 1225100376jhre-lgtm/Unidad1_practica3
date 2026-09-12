"""
Autor: Rosas Enriquez Jairo Haziel
Grupo: GTIR246
Inventario de Alumnos - Programacion de Redes

"""
import time
from tabulate import tabulate  # Librería para mostrar tablas con formato en consola


def mostrar_inventario(inventario):
    #Muestra en pantalla la lista de alumnos en formato de tabla.
    if len(inventario) == 0:
        print("El inventario esta vacio")
        return

    # Definimos los nombres de las columnas de la tabla
    encabezados = ["No.Control", "Nombre", "Apellidos", "Grupo", "Cuatrimestre"]
    filas = []
    for alumno in inventario:
        # Convertimos cada diccionario de alumno en una lista de valores (una fila)
        fila = [alumno["numero_control"], alumno["nombre"], alumno["apellidos"], alumno["grupo"], alumno["cuatrimestre"]]
        filas.append(fila)

    print()
    # Usamos tabulate para imprimir la tabla con bordes tipo "grid"
    print(tabulate(filas, headers=encabezados, tablefmt="grid"))
    print()


def agregar_elemento(inventario):
    #Solicita los datos de un nuevo alumno y lo agrega al inventario.
    print("\n-- Agregar alumno --")
    numero_control = input("Numero de control: ")

    # Validamos que el numero de control no este vacio
    if numero_control == "":
        print("El numero de control no puede estar vacio")
        return

    # Revisamos que no exista ya un alumno con ese numero de control (evitar duplicados)
    for alumno in inventario:
        if alumno["numero_control"] == numero_control:
            print("Ya existe un alumno con ese numero de control")
            return

    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    grupo = input("Grupo: ")

    # Validamos que los campos obligatorios no esten vacios
    if nombre == "" or apellidos == "" or grupo == "":
        print("Nombre, apellidos y grupo son obligatorios")
        return

    try:
        # Intentamos convertir el cuatrimestre a numero entero
        cuatrimestre = int(input("Cuatrimestre: "))
    except ValueError:
        # Si el usuario ingresa algo que no es un numero, mostramos error y salimos
        print("El cuatrimestre debe ser un numero")
        return

    # Creamos el diccionario con los datos del nuevo alumno
    alumno = {
        "numero_control": numero_control,
        "nombre": nombre,
        "apellidos": apellidos,
        "grupo": grupo,
        "cuatrimestre": cuatrimestre
    }

    # Agregamos el nuevo alumno a la lista del inventario
    inventario.append(alumno)
    print("Alumno agregado")
    time.sleep(1)  # Pausa breve para que el usuario pueda leer el mensaje


def buscar_elemento(inventario):
    #Busca alumnos cuyo numero de control o nombre coincida con el texto ingresado.
    if len(inventario) == 0:
        print("El inventario esta vacio")
        return

    # Convertimos el texto de busqueda a minusculas para comparar sin distinguir mayusculas/minusculas
    dato = input("Buscar por numero de control o nombre: ").lower()
    encontrado = False

    for alumno in inventario:
        # Comparamos si el texto buscado esta contenido en el numero de control o en el nombre
        if dato in alumno["numero_control"].lower() or dato in alumno["nombre"].lower():
            print(alumno)
            encontrado = True

    if not encontrado:
        print("No se encontro ningun alumno")
    time.sleep(1)


def editar_elemento(inventario):
    #Permite modificar el cuatrimestre de un alumno existente.
    if len(inventario) == 0:
        print("El inventario esta vacio")
        return

    numero_control = input("Numero de control del alumno a editar: ")

    # Recorremos el inventario buscando al alumno con ese numero de control
    for alumno in inventario:
        if alumno["numero_control"] == numero_control:
            try:
                # Solicitamos y validamos el nuevo valor de cuatrimestre
                nuevo_cuatrimestre = int(input("Nuevo cuatrimestre: "))
                alumno["cuatrimestre"] = nuevo_cuatrimestre
                print("Alumno actualizado")
                time.sleep(1)
            except ValueError:
                print("El cuatrimestre debe ser un numero entero")
            return  # Salimos de la funcion una vez encontrado (o fallido) el intento de edicion

    # Si el bucle termina sin encontrar coincidencia, mostramos este mensaje
    print("No se encontro un alumno con ese numero de control")


def eliminar_elemento(inventario):
    #Elimina un alumno del inventario dado su numero de control.
    if len(inventario) == 0:
        print("El inventario esta vacio")
        return

    numero_control = input("Numero de control del alumno a eliminar: ")

    # Buscamos al alumno y lo eliminamos de la lista si coincide el numero de control
    for alumno in inventario:
        if alumno["numero_control"] == numero_control:
            inventario.remove(alumno)
            print("Alumno eliminado")
            time.sleep(1)
            return

    print("No se encontro un alumno con ese numero de control")