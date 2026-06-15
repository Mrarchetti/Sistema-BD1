def registrar_asistencia(id_inscripcion, fecha, asistio, conexion, cursor):

    cursor.execute("""
        INSERT INTO asistencia
        (id_inscripcion, fecha, asistio)
        VALUES (%s, %s, %s)
    """, (id_inscripcion, fecha, asistio))

    conexion.commit()

    print("Asistencia registrada")


def listar_asistencias(conexion, cursor):

    cursor.execute("SELECT * FROM asistencia")

    for fila in cursor.fetchall():
        print(fila)


def modificar_asistencia(
    id_asistencia,
    id_inscripcion,
    fecha,
    asistio,
    conexion,
    cursor
):

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

    print("Asistencia actualizada")


def eliminar_asistencia(id_asistencia, conexion, cursor):
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
    return None