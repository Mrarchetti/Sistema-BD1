from funciones.estudiantes.estudiante_info import (
    crear_estudiante,
    listar_estudiantes,
    modificar_estudiante,
    eliminar_estudiante
)

from funciones.disciplinas.disciplina_info import (
    crear_disciplina,
    listar_disciplinas,
    modificar_disciplina,
    eliminar_disciplina
)

from funciones.espacios.espacio_info import (
    crear_espacio,
    listar_espacios,
    actualizar_espacio,
    eliminar_espacio
)

from funciones.actividades.actividad_info import (
    crear_actividad,
    listar_actividades,
    modificar_actividad,
    eliminar_actividad
)

from funciones.inscripciones.inscripcion_info import (
    inscribir_estudiante,
    listar_inscripciones,
    modificar_inscripcion,
    eliminar_inscripcion
)

from funciones.asistencias.asistencia_info import (
    registrar_asistencia,
    listar_asistencias,
    modificar_asistencia,
    eliminar_asistencia
)

from funciones.reportes.reporte_info import (
    actividades_mas_populares
)

from frontend.validaciones import (
    validar_documento_uruguayo,
    validar_no_vacio,
    validar_entero_positivo
)

def mostrar_menu():
    print("\n===== SISTEMA DEPORTIVO =====")
    print("1. Gestionar estudiantes")
    print("2. Gestionar disciplinas")
    print("3. Gestionar espacios")
    print("4. Gestionar actividades")
    print("5. Gestionar inscripciones")
    print("6. Gestionar asistencias")
    print("7. Reportes")
    print("0. Salir")


def menu_estudiantes(conexion, cursor):
    while True:
        print("\n--- ESTUDIANTES ---")
        print("1. Crear estudiante")
        print("2. Listar estudiantes")
        print("3. Modificar estudiante")
        print("4. Eliminar estudiante")
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

        elif opcion == "3":
            id_estudiante = int(input("ID estudiante: "))
            documento = input("Documento: ")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            correo = input("Correo: ")
            carrera = input("Carrera: ")
            facultad = input("Facultad: ")

            modificar_estudiante(
                id_estudiante,
                documento,
                nombre,
                apellido,
                correo,
                carrera,
                facultad,
                conexion,
                cursor
            )

        elif opcion == "4":
            listar_estudiantes(conexion, cursor)
            id_estudiante = int(input("ID estudiante a eliminar: "))

            if confirmar_eliminacion(f"el estudiante {id_estudiante}"):
                eliminar_estudiante(id_estudiante, conexion, cursor)
            else:
                print("Borrado cancelado")

        elif opcion == "0":
            break

        else:
            print("Opción inválida")

def menu_disciplinas(conexion, cursor):

    while True:

        print("\n--- DISCIPLINAS ---")
        print("1. Crear disciplina")
        print("2. Listar disciplinas")
        print("3. Modificar disciplina")
        print("4. Eliminar disciplina")
        print("0. Volver")

        opcion = input("Opción: ")

        if opcion == "1":

            nombre = input("Nombre: ")

            crear_disciplina(nombre, conexion, cursor)

        elif opcion == "2":

            listar_disciplinas(conexion, cursor)

        elif opcion == "3":

            id_disciplina = int(input("ID disciplina: "))
            nombre = input("Nuevo nombre: ")

            modificar_disciplina(id_disciplina, nombre, conexion, cursor)

        elif opcion == "4":

            listar_disciplinas(conexion, cursor)
            id_disciplina = int(input("ID disciplina a eliminar: "))

            if confirmar_eliminacion(f"la disciplina {id_disciplina}"):
                eliminar_disciplina(id_disciplina, conexion, cursor)
            else:
                print("Borrado cancelado")

        elif opcion == "0":

            break

def menu_espacios(conexion, cursor):

    while True:

        print("\n--- ESPACIOS ---")
        print("1. Crear espacio")
        print("2. Listar espacios")
        print("3. Actualizar espacio")
        print("4. Eliminar espacio")
        print("0. Volver")

        opcion = input("Opción: ")

        if opcion == "1":

            nombre = input("Nombre: ")
            ubicacion = input("Ubicación: ")

            crear_espacio(nombre, ubicacion, conexion, cursor)

        elif opcion == "2":

            listar_espacios(conexion, cursor)

        elif opcion == "3":

            id_espacio = int(input("ID espacio: "))
            nombre = input("Nuevo nombre: ")
            ubicacion = input("Nueva ubicación: ")

            actualizar_espacio(id_espacio, nombre, ubicacion, conexion, cursor)

        elif opcion == "4":

            listar_espacios(conexion, cursor)
            id_espacio = int(input("ID espacio: "))

            if confirmar_eliminacion(f"el espacio {id_espacio}"):
                eliminar_espacio(id_espacio, conexion, cursor)
            else:
                print("Borrado cancelado")

        elif opcion == "0":

            break

        else:

            print("Opción inválida")

def menu_inscripciones(conexion, cursor):

    while True:

        print("\n--- INSCRIPCIONES ---")
        print("1. Inscribir estudiante")
        print("2. Listar inscripciones")
        print("3. Modificar inscripción")
        print("4. Eliminar inscripción")
        print("0. Volver")

        opcion = input("Opción: ")

        if opcion == "1":

            id_estudiante = int(
                input("ID estudiante: ")
            )

            id_actividad = int(
                input("ID actividad: ")
            )

            estado = input("Estado (CONFIRMADA/ESPERA): ")

            inscribir_estudiante(
                id_estudiante,
                id_actividad,
                estado,
                conexion,
                cursor
            )

        elif opcion == "2":

            listar_inscripciones(conexion, cursor)

        elif opcion == "3":

            id_inscripcion = int(input("ID inscripción: "))
            id_estudiante = int(input("ID estudiante: "))
            id_actividad = int(input("ID actividad: "))
            estado = input("Estado (CONFIRMADA/ESPERA): ")

            modificar_inscripcion(
                id_inscripcion,
                id_estudiante,
                id_actividad,
                estado,
                conexion,
                cursor
            )

        elif opcion == "4":

            listar_inscripciones(conexion, cursor)
            id_inscripcion = int(input("ID inscripción a eliminar: "))

            if confirmar_eliminacion(f"la inscripción {id_inscripcion}"):
                eliminar_inscripcion(id_inscripcion, conexion, cursor)
            else:
                print("Borrado cancelado")

        elif opcion == "0":

            break

def menu_actividades(conexion, cursor):

    while True:

        print("\n--- ACTIVIDADES ---")
        print("1. Crear actividad")
        print("2. Listar actividades")
        print("3. Modificar actividad")
        print("4. Eliminar actividad")
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
                horario,
                conexion,
                cursor
            )

        elif opcion == "2":

            listar_actividades(conexion, cursor)

        elif opcion == "3":

            id_actividad = int(input("ID actividad: "))
            nombre = input("Nombre: ")
            id_disciplina = int(input("ID disciplina: "))
            id_espacio = int(input("ID espacio: "))
            cupo = int(input("Cupo máximo: "))
            dia = input("Día: ")
            horario = input("Horario (HH:MM:SS): ")
            estado = input("Estado (ABIERTA/CERRADA/FINALIZADA/CANCELADA): ")

            modificar_actividad(
                id_actividad,
                nombre,
                id_disciplina,
                id_espacio,
                cupo,
                dia,
                horario,
                estado,
                conexion,
                cursor
            )

        elif opcion == "4":

            listar_actividades(conexion, cursor)
            id_actividad = int(input("ID actividad a eliminar: "))

            if confirmar_eliminacion(f"la actividad {id_actividad}"):
                eliminar_actividad(id_actividad, conexion, cursor)
            else:
                print("Borrado cancelado")

        elif opcion == "0":

            break


def menu_asistencias(conexion, cursor):

    while True:

        print("\n--- ASISTENCIAS ---")
        print("1. Registrar asistencia")
        print("2. Listar asistencias")
        print("3. Modificar asistencia")
        print("4. Eliminar asistencia")
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
                asistio,
                conexion,
                cursor
            )

        elif opcion == "2":

            listar_asistencias(conexion, cursor)

        elif opcion == "3":

            id_asistencia = int(input("ID asistencia: "))
            id_inscripcion = int(input("ID inscripción: "))
            fecha = input("Fecha (AAAA-MM-DD): ")
            asistio = input("¿Asistió? (S/N): ").strip().upper() == "S"

            modificar_asistencia(
                id_asistencia,
                id_inscripcion,
                fecha,
                asistio,
                conexion,
                cursor
            )

        elif opcion == "4":

            listar_asistencias(conexion, cursor)
            id_asistencia = int(input("ID asistencia a eliminar: "))

            if confirmar_eliminacion(f"la asistencia {id_asistencia}"):
                eliminar_asistencia(id_asistencia, conexion, cursor)
            else:
                print("Borrado cancelado")

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


def confirmar_eliminacion(etiqueta):
	confirmacion = input(f"Confirma eliminar {etiqueta}? (S/N): ")
	return confirmacion.strip().upper() == "S"