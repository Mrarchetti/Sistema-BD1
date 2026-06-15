from estudiantes.estudiante_info import (
    crear_estudiante,
    listar_estudiantes
)

from disciplinas.disciplina_info import (
    crear_disciplina,
    listar_disciplinas
)

from actividades.actividad_info import (
    crear_actividad
)

from inscripciones.inscripcion_info import (
    inscribir_estudiante
)

from asistencias.asistencia_info import (
    registrar_asistencia
)

from reportes.reporte_info import (
    actividades_mas_populares
)

import mysql.connector
from mysql.connector import Error


DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "rootpassword",
    "database": "actividades_deportivas",
    "autocommit": False,
}

def conectar():
    return mysql.connector.connect(**DB_CONFIG)

def mostrar_menu():
    print("\n===== SISTEMA DEPORTIVO =====")
    print("1. Gestionar estudiantes")
    print("2. Gestionar disciplinas")
    print("3. Gestionar actividades")
    print("4. Gestionar inscripciones")
    print("5. Gestionar asistencias")
    print("6. Reportes")
    print("0. Salir")


def menu_estudiantes(conexion, cursor):
    while True:
        print("\n--- ESTUDIANTES ---")
        print("1. Crear estudiante")
        print("2. Listar estudiantes")
        print("0. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            documento = input("Documento: ")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            correo = input("Correo: ")
            carrera = input("Carrera: ")
            facultad = input("Facultad: ")

            crear_estudiante(
                documento,
                nombre,
                apellido,
                correo,
                carrera,
                facultad,
                conexion,
                cursor
            )

        elif opcion == "2":
            listar_estudiantes(conexion, cursor)

        elif opcion == "0":
            break

        else:
            print("Opción inválida")

def menu_disciplinas(conexion, cursor):

    while True:

        print("\n--- DISCIPLINAS ---")
        print("1. Crear disciplina")
        print("2. Listar disciplinas")
        print("0. Volver")

        opcion = input("Opción: ")

        if opcion == "1":

            nombre = input("Nombre: ")

            crear_disciplina(nombre, conexion, cursor)

        elif opcion == "2":

            listar_disciplinas(conexion, cursor)

        elif opcion == "0":

            break

def menu_actividades(conexion, cursor):

    while True:

        print("\n--- ACTIVIDADES ---")
        print("1. Crear actividad")
        print("0. Volver")

        opcion = input("Opción: ")

        if opcion == "1":

            nombre = input("Nombre: ")

            id_disciplina = int(
                input("ID disciplina: ")
            )

            id_espacio = int(
                input("ID espacio: ")
            )

            cupo = int(
                input("Cupo máximo: ")
            )

            dia = input("Día: ")

            horario = input("Horario (HH:MM:SS): ")

            crear_actividad(conexion, cursor)

        elif opcion == "0":

            break

def menu_inscripciones(conexion, cursor):

    while True:

        print("\n--- INSCRIPCIONES ---")
        print("1. Inscribir estudiante")
        print("0. Volver")

        opcion = input("Opción: ")

        if opcion == "1":

            id_estudiante = int(
                input("ID estudiante: ")
            )

            id_actividad = int(
                input("ID actividad: ")
            )

            inscribir_estudiante(conexion, cursor)

        elif opcion == "0":

            break

def menu_asistencias(conexion, cursor):

    while True:

        print("\n--- ASISTENCIAS ---")
        print("1. Registrar asistencia")
        print("0. Volver")

        opcion = input("Opción: ")

        if opcion == "1":

            id_inscripcion = int(
                input("ID inscripción: ")
            )

            fecha = input(
                "Fecha (AAAA-MM-DD): "
            )

            asistio = input(
                "¿Asistió? (S/N): "
            )

            asistio = asistio.upper() == "S"

            registrar_asistencia(conexion, cursor)

        elif opcion == "0":

            break

def menu_reportes(conexion, cursor):

    while True:

        print("\n--- REPORTES ---")
        print("1. Actividades más populares")
        print("0. Volver")

        opcion = input("Opción: ")

        if opcion == "1":

            actividades_mas_populares(conexion, cursor)

        elif opcion == "0":

            break

def main():
    conexion = conectar()
    cursor = conexion.cursor()

    while True:

        mostrar_menu()

        opcion = input(
            "Seleccione una opción: "
        )

        if opcion == "1":

            menu_estudiantes(conexion,cursor)

        elif opcion == "2":

            menu_disciplinas(conexion,cursor)

        elif opcion == "3":

            menu_actividades(conexion,cursor)

        elif opcion == "4":

            menu_inscripciones(conexion,cursor)

        elif opcion == "5":

            menu_asistencias(conexion,cursor)

        elif opcion == "6":

            menu_reportes(conexion,cursor)

        elif opcion == "0":
            
            cursor.close()
            conexion.close()
            print("Hasta luego")
            break

        else:

            print("Opción inválida")

if __name__ == "__main__":
    main()