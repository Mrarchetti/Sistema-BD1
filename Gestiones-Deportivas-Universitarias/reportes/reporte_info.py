def actividades_populares():

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT
            a.nombre,
            COUNT(*) cantidad
        FROM actividad a
        JOIN inscripcion i
        ON a.id_actividad=i.id_actividad
        WHERE i.estado='CONFIRMADA'
        GROUP BY a.id_actividad
        ORDER BY cantidad DESC
    """)

    for fila in cursor.fetchall():
        print(fila)

    cursor.close()
    conexion.close()


def actividades_con_cupo():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT
            a.nombre,
            a.cupo_maximo -
            COUNT(i.id_inscripcion)
        FROM actividad a
        LEFT JOIN inscripcion i
        ON a.id_actividad=i.id_actividad
        AND i.estado='CONFIRMADA'
        GROUP BY a.id_actividad
    """)

    for fila in cursor.fetchall():
        print(fila)

    cursor.close()
    conexion.close()