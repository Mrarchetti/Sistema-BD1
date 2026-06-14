def crear_espacio(
    nombre,
    ubicacion
):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO espacio
        (
            nombre,
            ubicacion
        )
        VALUES(%s,%s)
    """,(nombre,ubicacion))

    conexion.commit()

    print("Espacio creado")

    cursor.close()
    conexion.close()


def listar_espacios():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT *
        FROM espacio
    """)

    for fila in cursor.fetchall():
        print(fila)

    cursor.close()
    conexion.close()