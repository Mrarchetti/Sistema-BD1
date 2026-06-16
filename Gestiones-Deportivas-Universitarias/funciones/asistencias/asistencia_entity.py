from funciones.validaciones import (
    validar_entero_positivo,
    validar_fecha,
    validar_confirmacion
)
from funciones.inscripciones.inscripcion_entity import (
    buscar_inscripcion_por_id
)

def registrar_asistencia(id_inscripcion, fecha, asistio, conexion, cursor):

    if not validar_entero_positivo(id_inscripcion)[0]:
        return False
    if buscar_inscripcion_por_id(id_inscripcion, conexion, cursor) is None:
        return False
    if not validar_fecha(fecha)[0]:
        return False
    if not validar_confirmacion(asistio)[0]:
        return False
    
    cursor.execute("""
        INSERT INTO asistencia
        (id_inscripcion, fecha, asistio)
        VALUES (%s, %s, %s)
    """, (id_inscripcion, fecha, asistio))

    conexion.commit()
    return True



def listar_asistencias(conexion, cursor):

    cursor.execute("SELECT * FROM asistencia")

    return cursor.fetchall()


def modificar_asistencia(
    id_asistencia,
    id_inscripcion,
    fecha,
    asistio,
    conexion,
    cursor
):
    if not validar_entero_positivo(id_asistencia)[0]:
        return False
    if buscar_asistencia_por_id(id_asistencia, conexion, cursor) is None:
        return False
    if not validar_entero_positivo(id_inscripcion)[0]:
        return False
    if not validar_fecha(fecha)[0]:
        return False
    if not validar_confirmacion(asistio)[0]:
        return False
    cursor.execute("""
        UPDATE asistencia
        SET id_inscripcion=%s,
            fecha=%s,
            asistio=%s
        WHERE id_asistencia=%s
    """, (
        id_inscripcion,
        fecha,
        asistio,
        id_asistencia
    ))

    conexion.commit()
    return True


def eliminar_asistencia(id_asistencia, conexion, cursor):
    if not validar_entero_positivo(id_asistencia)[0]:
        return False
    if buscar_asistencia_por_id(id_asistencia, conexion, cursor) is None:
        return False
    try:
        cursor.execute(
            "DELETE FROM asistencia WHERE id_asistencia=%s",
            (id_asistencia,)
        )
        conexion.commit()
        return True
    except Exception as e:
        conexion.rollback()
        return False
    
def buscar_asistencia_por_id(id_asistencia, conexion, cursor):
    if not validar_entero_positivo(id_asistencia)[0]:
        return None
    cursor.execute("""
        SELECT *
        FROM asistencia
        WHERE id_asistencia=%s
    """, (id_asistencia,))

    return cursor.fetchone()