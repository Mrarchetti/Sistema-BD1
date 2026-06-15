def inscribir_estudiante(id_estudiante, id_actividad, estado, conexion, cursor):

    cursor.execute("""
        INSERT INTO inscripcion
        (id_estudiante, id_actividad, estado)
        VALUES (%s, %s, %s)
    """, (id_estudiante, id_actividad, estado))

    conexion.commit()

    print("Inscripción creada")


def listar_inscripciones(conexion, cursor):

    cursor.execute("SELECT * FROM inscripcion")

    for fila in cursor.fetchall():
        print(fila)


def modificar_inscripcion(
    id_inscripcion,
    id_estudiante,
    id_actividad,
    estado,
    conexion,
    cursor
):

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

    print("Inscripción actualizada")


def eliminar_inscripcion(id_inscripcion, conexion, cursor):

    cursor.execute(
        "DELETE FROM inscripcion WHERE id_inscripcion=%s",
        (id_inscripcion,)
    )

    conexion.commit()

    print("Inscripción eliminada")