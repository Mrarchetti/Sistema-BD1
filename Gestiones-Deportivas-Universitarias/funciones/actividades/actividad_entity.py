from funciones.validaciones import (
    validar_no_vacio,
    validar_entero_positivo,
    validar_horario,
    validar_estado
)
from funciones.disciplinas.disciplina_entity import (
    buscar_disciplina_por_id
)
from funciones.espacios.espacio_entity import (
    buscar_espacio_por_id
)


def crear_actividad(
    nombre,
    id_disciplina,
    id_espacio,
    cupo_maximo,
    dia,
    horario,
    conexion,
    cursor
):
    if not validar_no_vacio(nombre)[0]:
        return False
    if not validar_entero_positivo(id_disciplina)[0]:
        return False
    if not validar_entero_positivo(id_espacio)[0]:
        return False
    if not validar_entero_positivo(cupo_maximo)[0]:
        return False
    if not validar_no_vacio(dia)[0]:
        return False
    if not validar_horario(horario)[0]:
        return False
    
    cursor.execute("""
        INSERT INTO actividad
        (nombre, id_disciplina, id_espacio, cupo_maximo, dia, horario)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        nombre,
        id_disciplina,
        id_espacio,
        cupo_maximo,
        dia,
        horario
    ))

    conexion.commit()
    return True



def listar_actividades(conexion, cursor):

    cursor.execute("SELECT * FROM actividad")

    return cursor.fetchall()


def modificar_actividad(
    id_actividad,
    nombre,
    id_disciplina,
    id_espacio,
    cupo_maximo,
    dia,
    horario,
    estado,
    conexion,
    cursor
):
    if buscar_actividad_por_id(id_actividad, conexion, cursor) is None:
        return False
    if not validar_no_vacio(nombre)[0]:
        return False
    if not validar_entero_positivo(id_disciplina)[0]:
        return False
    if buscar_disciplina_por_id(id_disciplina, conexion, cursor) is None:
        return False
    if not validar_entero_positivo(id_espacio)[0]:
        return False
    if buscar_espacio_por_id(id_espacio, conexion, cursor) is None:
        return False
    if not validar_entero_positivo(cupo_maximo)[0]:
        return False
    if not validar_no_vacio(dia)[0]:
        return False
    if not validar_horario(horario)[0]:
        return False
    if not validar_estado(estado)[0]:
        return False

    cursor.execute("""
        UPDATE actividad
        SET nombre=%s,
            id_disciplina=%s,
            id_espacio=%s,
            cupo_maximo=%s,
            dia=%s,
            horario=%s,
            estado=%s
        WHERE id_actividad=%s
    """, (
        nombre,
        id_disciplina,
        id_espacio,
        cupo_maximo,
        dia,
        horario,
        estado,
        id_actividad
    ))

    conexion.commit()
    return True



def eliminar_actividad(id_actividad, conexion, cursor):
    if not validar_entero_positivo(id_actividad)[0]:
        return False
    if buscar_actividad_por_id(id_actividad, conexion, cursor) is None:
        return False
    try:
        cursor.execute(
            "DELETE FROM actividad WHERE id_actividad=%s",
            (id_actividad,)
        )
        conexion.commit()
        return True
    except Exception as e:
        conexion.rollback()
        return False
    
def buscar_actividad_por_id(id_actividad, conexion, cursor):
    if not validar_entero_positivo(id_actividad)[0]:
        return None
    cursor.execute("""
        SELECT *
        FROM actividad
        WHERE id_actividad=%s
    """, (id_actividad,))
    return cursor.fetchone()
