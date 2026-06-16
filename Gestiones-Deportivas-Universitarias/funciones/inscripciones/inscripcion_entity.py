from funciones.estudiantes.estudiante_entity import buscar_estudiante_por_id
from funciones.actividades.actividad_entity import buscar_actividad_por_id
from funciones.validaciones import (
    validar_entero_positivo,
    validar_estado
)

def inscribir_estudiante(id_estudiante, id_actividad, estado, conexion, cursor):
    if not validar_entero_positivo(id_estudiante)[0]:
        return False
    if buscar_estudiante_por_id(id_estudiante, conexion, cursor) is None:
        return False
    if not validar_entero_positivo(id_actividad)[0]:
        return False
    if buscar_actividad_por_id(id_actividad, conexion, cursor) is None:
        return False
    if not validar_estado(estado)[0]:
        return False
    
    cursor.execute("""
        INSERT INTO inscripcion
        (id_estudiante, id_actividad, estado)
        VALUES (%s, %s, %s)
    """, (id_estudiante, id_actividad, estado))

    conexion.commit()



def listar_inscripciones(conexion, cursor):

    cursor.execute("SELECT * FROM inscripcion")

    return cursor.fetchall()


def modificar_inscripcion(
    id_inscripcion,
    id_estudiante,
    id_actividad,
    estado,
    conexion,
    cursor
):
    if not validar_entero_positivo(id_inscripcion)[0]:
        return False
    if buscar_inscripcion_por_id(id_inscripcion, conexion, cursor) is None:
        return False
    if not validar_entero_positivo(id_estudiante)[0]:
        return False
    if buscar_estudiante_por_id(id_estudiante, conexion, cursor) is None:
        return False
    if not validar_entero_positivo(id_actividad)[0]:
        return False
    if buscar_actividad_por_id(id_actividad, conexion, cursor) is None:
        return False
    if not validar_estado(estado)[0]:
        return False
    
    cursor.execute("""
        UPDATE inscripcion
        SET id_estudiante=%s,
            id_actividad=%s,
            estado=%s
        WHERE id_inscripcion=%s
    """, (
        id_estudiante,
        id_actividad,
        estado,
        id_inscripcion
    ))

    conexion.commit()



def eliminar_inscripcion(id_inscripcion, conexion, cursor):
    if not validar_entero_positivo(id_inscripcion)[0]:
        return False
    if buscar_inscripcion_por_id(id_inscripcion, conexion, cursor) is None:
        return False
    try:
        cursor.execute(
            "DELETE FROM inscripcion WHERE id_inscripcion=%s",
            (id_inscripcion,)
        )
        conexion.commit()
        return True
    except Exception as e:
        conexion.rollback()
        return False
    
def buscar_inscripcion_por_id(id_inscripcion, conexion, cursor):
    if not validar_entero_positivo(id_inscripcion)[0]:
        return None
    if buscar_inscripcion_por_id(id_inscripcion, conexion, cursor) is None:
        return None

    cursor.execute("""
        SELECT *
        FROM inscripcion
        WHERE id_inscripcion=%s
    """, (id_inscripcion,))

    return cursor.fetchone()