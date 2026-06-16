def actividades_populares(conexion, cursor):

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

    return cursor.fetchall()



def actividades_con_cupo(conexion, cursor):

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

    return cursor.fetchall()



def actividades_mas_populares(conexion, cursor):

    cursor.execute("""
        SELECT
            a.id_actividad,
            a.nombre,
            COUNT(i.id_inscripcion) AS cantidad_confirmados
        FROM actividad a
        LEFT JOIN inscripcion i
            ON a.id_actividad = i.id_actividad
           AND i.estado = 'CONFIRMADA'
        GROUP BY a.id_actividad, a.nombre
        ORDER BY cantidad_confirmados DESC
    """)

    return cursor.fetchall()