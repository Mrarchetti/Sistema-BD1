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

    print("Actividad creada")


def listar_actividades(conexion, cursor):

    cursor.execute("SELECT * FROM actividad")

    for fila in cursor.fetchall():
        print(fila)


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

    print("Actividad actualizada")


def eliminar_actividad(id_actividad, conexion, cursor):
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
    return None