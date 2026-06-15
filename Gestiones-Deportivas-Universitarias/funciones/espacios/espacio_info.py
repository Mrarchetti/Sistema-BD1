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
    try:
        cursor.execute(
            "DELETE FROM espacio WHERE id_espacio=%s",
            (id_espacio,)
        )
        conexion.commit()
        return True
    except Exception as e:
        conexion.rollback()
        return False

def buscar_espacio_por_id(id_espacio, conexion, cursor):
    return None