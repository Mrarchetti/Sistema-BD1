
from frontend.menus import (
    mostrar_menu,
    menu_estudiantes,
    menu_disciplinas,
    menu_actividades,
    menu_inscripciones,
    menu_asistencias,
    menu_reportes,
    menu_espacios
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

        elif opcion == "7":

            menu_espacios(conexion,cursor)

        elif opcion == "0":
            
            cursor.close()
            conexion.close()
            print("Hasta luego")
            break

        else:

            print("Opción inválida")

if __name__ == "__main__":
    main()