from funciones.estudiantes.estudiante_info import (
    crear_estudiante,
    listar_estudiantes,
    buscar_estudiante_por_documento,
    modificar_estudiante,
    eliminar_estudiante
)

from funciones.disciplinas.disciplina_info import (
    crear_disciplina,
    listar_disciplinas,
    modificar_disciplina,
    eliminar_disciplina,
    buscar_disciplina_por_id
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
    validar_entero_positivo,
    pedir_hasta_valido,
    pedir_hasta_valido_modif
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
            documento = pedir_hasta_valido("Documento: ", validar_documento_uruguayo)
            nombre = pedir_hasta_valido("Nombre: ", validar_no_vacio)
            apellido = pedir_hasta_valido("Apellido: ", validar_no_vacio)
            correo = pedir_hasta_valido("Correo: ", validar_no_vacio)
            carrera = pedir_hasta_valido("Carrera: ", validar_no_vacio)
            facultad = pedir_hasta_valido("Facultad: ", validar_no_vacio)

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

            documento = pedir_hasta_valido("Documento del estudiante: ", validar_documento_uruguayo)
            estudiante = buscar_estudiante_por_documento(documento, conexion, cursor)

            if estudiante is None:
                print("No se encontró un estudiante con ese documento")
                continue

            id_estudiante = estudiante[0]
            print("Estudiante encontrado:", estudiante, "\nIngrese los nuevos datos(para mantener los actuales mantener vacio):")

            documento = pedir_hasta_valido_modif("Nuevo documento: ", estudiante[1], validar_documento_uruguayo)
            nombre = pedir_hasta_valido_modif("Nuevo nombre: ", estudiante[2], validar_no_vacio)
            apellido = pedir_hasta_valido_modif("Nuevo apellido: ", estudiante[3], validar_no_vacio)
            correo = pedir_hasta_valido_modif("Nuevo correo: ", estudiante[4], validar_no_vacio)
            carrera = pedir_hasta_valido_modif("Nueva carrera: ", estudiante[5], validar_no_vacio)
            facultad = pedir_hasta_valido_modif("Nueva facultad: ", estudiante[6], validar_no_vacio)

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
            documento = pedir_hasta_valido("Documento del estudiante a eliminar: ", validar_documento_uruguayo)
            estudiante = buscar_estudiante_por_documento(documento, conexion, cursor)

            if estudiante is None:
                print("No se encontró un estudiante con ese documento")
                continue

            id_estudiante = estudiante[0]

            if confirmar_eliminacion(f"el estudiante {id_estudiante}"):
                if eliminar_estudiante(id_estudiante, conexion, cursor):
                    print("Estudiante eliminado exitosamente")
                else:
                    print("No se pudo eliminar el estudiante. Puede que tenga inscripciones asociadas.")
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

            nombre = pedir_hasta_valido("Nombre: ", validar_no_vacio)

            crear_disciplina(nombre, conexion, cursor)
            print("Disciplina creada exitosamente")

        elif opcion == "2":

            listar_disciplinas(conexion, cursor)

        elif opcion == "3":
            id_disciplina = int(pedir_hasta_valido("ID disciplina a modificar: ", validar_entero_positivo))
            disciplina = buscar_disciplina_por_id(id_disciplina, conexion, cursor)

            if disciplina is None:
                print("No se encontró una disciplina con ese ID")
                continue
            nombre = pedir_hasta_valido("Nuevo nombre: ", validar_no_vacio)
            modificar_disciplina(id_disciplina, nombre, conexion, cursor)
            print("Disciplina actualizada exitosamente")

        elif opcion == "4":

            id_disciplina = int(pedir_hasta_valido("ID disciplina a eliminar: ", validar_entero_positivo))
            disciplina = buscar_disciplina_por_id(id_disciplina, conexion, cursor)

            if disciplina is None:
                print("No se encontró una disciplina con ese ID")
                continue

            if confirmar_eliminacion(f"la disciplina {id_disciplina}"):
                if eliminar_disciplina(id_disciplina, conexion, cursor):
                    print("Disciplina eliminada exitosamente")
                else:
                    print("No se pudo eliminar la disciplina. Puede que tenga actividades asociadas.")
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

            nombre = pedir_hasta_valido("Nombre: ", validar_no_vacio)
            ubicacion = pedir_hasta_valido("Ubicación: ", validar_no_vacio)

            crear_espacio(nombre, ubicacion, conexion, cursor)
            print("Espacio creado exitosamente")

        elif opcion == "2":

            listar_espacios(conexion, cursor)

        elif opcion == "3":
            id_espacio = int(pedir_hasta_valido("ID espacio a actualizar: ", validar_entero_positivo))
            nombre = pedir_hasta_valido("Nuevo nombre: ", validar_no_vacio)
            ubicacion = pedir_hasta_valido("Nueva ubicación: ", validar_no_vacio)

            actualizar_espacio(id_espacio, nombre, ubicacion, conexion, cursor)
            print("Espacio actualizado exitosamente")

        elif opcion == "4":

            id_espacio = int(pedir_hasta_valido("ID espacio a eliminar: ", validar_entero_positivo))

            if confirmar_eliminacion(f"el espacio {id_espacio}"):
                if eliminar_espacio(id_espacio, conexion, cursor):
                    print("Espacio eliminado exitosamente")
                else:
                    print("No se pudo eliminar el espacio. Puede que tenga actividades asociadas.")
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

            id_estudiante = int(pedir_hasta_valido("ID estudiante: ", validar_entero_positivo))
            id_actividad = int(pedir_hasta_valido("ID actividad: ", validar_entero_positivo))
            estado = pedir_hasta_valido("Estado (CONFIRMADA/ESPERA): ", validar_no_vacio)

            inscribir_estudiante(
                id_estudiante,
                id_actividad,
                estado,
                conexion,
                cursor
            )
            print("Inscripción creada exitosamente")

        elif opcion == "2":

            listar_inscripciones(conexion, cursor)

        elif opcion == "3":

            id_inscripcion = int(pedir_hasta_valido("ID inscripción a modificar: ", validar_entero_positivo))
            id_estudiante = int(pedir_hasta_valido("ID estudiante: ", validar_entero_positivo))
            id_actividad = int(pedir_hasta_valido("ID actividad: ", validar_entero_positivo))
            estado = pedir_hasta_valido("Estado (CONFIRMADA/ESPERA): ", validar_no_vacio)

            modificar_inscripcion(
                id_inscripcion,
                id_estudiante,
                id_actividad,
                estado,
                conexion,
                cursor
            )
            print("Inscripción actualizada exitosamente")

        elif opcion == "4":

            id_inscripcion = int(pedir_hasta_valido("ID inscripción a eliminar: ", validar_entero_positivo))

            if confirmar_eliminacion(f"la inscripción {id_inscripcion}"):
                if eliminar_inscripcion(id_inscripcion, conexion, cursor):
                    print("Inscripción eliminada exitosamente")
                else:
                    print("No se pudo eliminar la inscripción.")
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

            nombre = pedir_hasta_valido("Nombre: ", validar_no_vacio)
            id_disciplina = int(pedir_hasta_valido("ID disciplina: ", validar_entero_positivo))
            id_espacio = int(pedir_hasta_valido("ID espacio: ", validar_entero_positivo))
            cupo = int(pedir_hasta_valido("Cupo máximo: ", validar_entero_positivo))
            dia = pedir_hasta_valido("Día: ", validar_no_vacio)
            horario = pedir_hasta_valido("Horario (HH:MM:SS): ", validar_no_vacio)

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
            print("Actividad creada exitosamente")

        elif opcion == "2":

            listar_actividades(conexion, cursor)

        elif opcion == "3":

            id_actividad = int(pedir_hasta_valido("ID actividad a modificar: ", validar_entero_positivo))
            nombre = pedir_hasta_valido("Nombre: ", validar_no_vacio)
            id_disciplina = int(pedir_hasta_valido("ID disciplina: ", validar_entero_positivo))
            id_espacio = int(pedir_hasta_valido("ID espacio: ", validar_entero_positivo))
            cupo = int(pedir_hasta_valido("Cupo máximo: ", validar_entero_positivo))
            dia = pedir_hasta_valido("Día: ", validar_no_vacio)
            horario = pedir_hasta_valido("Horario (HH:MM:SS): ", validar_no_vacio)
            estado = pedir_hasta_valido("Estado (ABIERTA/CERRADA/FINALIZADA/CANCELADA): ", validar_no_vacio)

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
            print("Actividad actualizada exitosamente")

        elif opcion == "4":

            id_actividad = int(pedir_hasta_valido("ID actividad a eliminar: ", validar_entero_positivo))

            if confirmar_eliminacion(f"la actividad {id_actividad}"):
                if eliminar_actividad(id_actividad, conexion, cursor):
                    print("Actividad eliminada exitosamente")
                else:
                    print("No se pudo eliminar la actividad. Puede que tenga inscripciones asociadas.")
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

            id_inscripcion = int(pedir_hasta_valido("ID inscripción: ", validar_entero_positivo))
            fecha = pedir_hasta_valido("Fecha (AAAA-MM-DD): ", validar_no_vacio)
            asistio = pedir_hasta_valido("¿Asistió? (S/N): ", validar_no_vacio)
            asistio = asistio.upper() == "S"

            registrar_asistencia(
                id_inscripcion,
                fecha,
                asistio,
                conexion,
                cursor
            )
            print("Asistencia registrada exitosamente")

        elif opcion == "2":

            listar_asistencias(conexion, cursor)

        elif opcion == "3":

            id_asistencia = int(pedir_hasta_valido("ID asistencia a modificar: ", validar_entero_positivo))
            id_inscripcion = int(pedir_hasta_valido("ID inscripción: ", validar_entero_positivo))
            fecha = pedir_hasta_valido("Fecha (AAAA-MM-DD): ", validar_no_vacio)
            asistio = pedir_hasta_valido("¿Asistió? (S/N): ", validar_no_vacio).strip().upper() == "S"

            modificar_asistencia(
                id_asistencia,
                id_inscripcion,
                fecha,
                asistio,
                conexion,
                cursor
            )
            print("Asistencia actualizada exitosamente")

        elif opcion == "4":

            id_asistencia = int(pedir_hasta_valido("ID asistencia a eliminar: ", validar_entero_positivo))

            if confirmar_eliminacion(f"la asistencia {id_asistencia}"):
                if eliminar_asistencia(id_asistencia, conexion, cursor):
                    print("Asistencia eliminada exitosamente")
                else:
                    print("No se pudo eliminar la asistencia.")
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