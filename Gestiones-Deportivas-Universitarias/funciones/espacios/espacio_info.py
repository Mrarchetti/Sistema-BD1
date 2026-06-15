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


def actualizar_espacio(id_espacio, nombre, ubicacion, conexion, cursor):

    cursor.execute("""
        UPDATE espacio
        SET nombre=%s, ubicacion=%s
        WHERE id_espacio=%s
    """, (nombre, ubicacion, id_espacio))

    conexion.commit()

    print("Espacio actualizado")


def eliminar_espacio(id_espacio, conexion, cursor):

    cursor.execute(
        "DELETE FROM espacio WHERE id_espacio=%s",
        (id_espacio,)
    )

    conexion.commit()

    print("Espacio eliminado")
