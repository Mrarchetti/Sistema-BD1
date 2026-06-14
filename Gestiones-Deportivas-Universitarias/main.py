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

import sqlite3


def conectar(db_path: str = "sistema.db"):
    """Crear y devolver una conexión SQLite.

    Se usa una base de datos local por defecto. Ajustar según sea necesario.
    """
    return sqlite3.connect(db_path)

def mostrar_menu():
    print("\n===== SISTEMA DEPORTIVO =====")
    print("1. Gestionar estudiantes")
    print("2. Gestionar disciplinas")
    print("3. Gestionar actividades")
    print("4. Gestionar inscripciones")
    print("5. Gestionar asistencias")
    print("6. Reportes")
    print("0. Salir")


def menu_estudiantes():
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
                facultad
            )

        elif opcion == "2":
            listar_estudiantes()

        elif opcion == "0":
            break

        else:
            print("Opción inválida")

def menu_disciplinas():

    while True:

        print("\n--- DISCIPLINAS ---")
        print("1. Crear disciplina")
        print("2. Listar disciplinas")
        print("0. Volver")

        opcion = input("Opción: ")

        if opcion == "1":

            nombre = input("Nombre: ")

            crear_disciplina(nombre)

        elif opcion == "2":

            listar_disciplinas()

        elif opcion == "0":

            break

def menu_actividades():

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

            crear_actividad(
                nombre,
                id_disciplina,
                id_espacio,
                cupo,
                dia,
                horario
            )

        elif opcion == "0":

            break

def menu_inscripciones():

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

            inscribir_estudiante(
                id_estudiante,
                id_actividad
            )

        elif opcion == "0":

            break

def menu_asistencias():

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

            registrar_asistencia(
                id_inscripcion,
                fecha,
                asistio
            )

        elif opcion == "0":

            break

def menu_reportes():

    while True:

        print("\n--- REPORTES ---")
        print("1. Actividades más populares")
        print("0. Volver")

        opcion = input("Opción: ")

        if opcion == "1":

            actividades_mas_populares()

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

            menu_estudiantes()

        elif opcion == "2":

            menu_disciplinas()

        elif opcion == "3":

            menu_actividades()

        elif opcion == "4":

            menu_inscripciones()

        elif opcion == "5":

            menu_asistencias()

        elif opcion == "6":

            menu_reportes()

        elif opcion == "0":

            print("Hasta luego")
            break

        else:

            print("Opción inválida")

if __name__ == "__main__":
    main()