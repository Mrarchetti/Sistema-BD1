def crear_espacio(nombre,ubicacion,conexion, cursor):


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


def listar_espacios(conexion,cursor):

    cursor.execute("""
        SELECT *
        FROM espacio
    """)

    for fila in cursor.fetchall():
        print(fila)
