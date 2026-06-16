from funciones.validaciones import (
    validar_no_vacio,
    validar_entero_positivo,
    validar_documento_uruguayo
)


def crear_estudiante(
    documento,
    nombre,
    apellido,
    correo,
    carrera,
    facultad,
    conexion,
    cursor
):
    if not validar_documento_uruguayo(documento)[0]:
        return False
    if not validar_no_vacio(nombre)[0]:
        return False
    if not validar_no_vacio(apellido)[0]:
        return False
    if not validar_no_vacio(correo)[0]:
        return False
    if not validar_no_vacio(carrera)[0]:
        return False
    if not validar_no_vacio(facultad)[0]:
        return False

    cursor.execute("""
        INSERT INTO estudiante
        (documento, nombre, apellido, correo, carrera, facultad)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        documento,
        nombre,
        apellido,
        correo,
        carrera,
        facultad
    ))

    conexion.commit()
    return True


def listar_estudiantes(conexion, cursor):

    cursor.execute("SELECT * FROM estudiante")

    return cursor.fetchall()


def buscar_estudiante_por_documento(documento, conexion, cursor):
    if not validar_documento_uruguayo(documento)[0]:
        return None

    cursor.execute("""
        SELECT *
        FROM estudiante
        WHERE documento=%s
    """, (documento,))

    return cursor.fetchone()


def buscar_estudiante_por_id(id_estudiante, conexion, cursor):
    if not validar_entero_positivo(id_estudiante)[0]:
        return None
    if buscar_estudiante_por_id(id_estudiante, conexion, cursor) is None:
        return None

    cursor.execute("""
        SELECT *
        FROM estudiante
        WHERE id_estudiante=%s
    """, (id_estudiante,))

    return cursor.fetchone()


def modificar_estudiante(
    id_estudiante,
    documento,
    nombre,
    apellido,
    correo,
    carrera,
    facultad,
    conexion,
    cursor
):
    if not validar_entero_positivo(id_estudiante)[0]:
        return False
    if buscar_estudiante_por_id(id_estudiante, conexion, cursor) is None:
        return False
    if not validar_documento_uruguayo(documento)[0]:
        return False
    if not validar_no_vacio(nombre)[0]:
        return False
    if not validar_no_vacio(apellido)[0]:
        return False
    if not validar_no_vacio(correo)[0]:
        return False
    if not validar_no_vacio(carrera)[0]:
        return False
    if not validar_no_vacio(facultad)[0]:
        return False

    cursor.execute("""
        UPDATE estudiante
        SET documento=%s,
            nombre=%s,
            apellido=%s,
            correo=%s,
            carrera=%s,
            facultad=%s
        WHERE id_estudiante=%s
    """, (
        documento,
        nombre,
        apellido,
        correo,
        carrera,
        facultad,
        id_estudiante
    ))

    conexion.commit()
    return True


def eliminar_estudiante(id_estudiante, conexion, cursor):
    if not validar_entero_positivo(id_estudiante)[0]:
        return False
    if buscar_estudiante_por_id(id_estudiante, conexion, cursor) is None:
        return False

    try:
        cursor.execute(
            "DELETE FROM estudiante WHERE id_estudiante=%s",
            (id_estudiante,)
        )
        conexion.commit()
        return True
    except Exception as e:
        conexion.rollback()
        return False