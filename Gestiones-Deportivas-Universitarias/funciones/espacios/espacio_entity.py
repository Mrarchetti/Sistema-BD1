def crear_espacio(nombre,ubicacion,conexion, cursor):
    if not validar_no_vacio(nombre)[0]:
        return False
    if not validar_no_vacio(ubicacion)[0]:
        return False

    cursor.execute("""
        INSERT INTO espacio
        (
            nombre,
            ubicacion
        )
        VALUES(%s,%s)
    """,(nombre,ubicacion))

    conexion.commit()




def listar_espacios(conexion,cursor):

    cursor.execute("""
        SELECT *
        FROM espacio
    """)

    return cursor.fetchall()


def actualizar_espacio(id_espacio, nombre, ubicacion, conexion, cursor):
    if not validar_entero_positivo(id_espacio)[0]:
        return False
    if buscar_espacio_por_id(id_espacio, conexion, cursor) is None:
        return False
    if not validar_no_vacio(nombre)[0]:
        return False
    if not validar_no_vacio(ubicacion)[0]:
        return False
    
    cursor.execute("""
        UPDATE espacio
        SET nombre=%s, ubicacion=%s
        WHERE id_espacio=%s
    """, (nombre, ubicacion, id_espacio))

    conexion.commit()



def eliminar_espacio(id_espacio, conexion, cursor):
    if not validar_entero_positivo(id_espacio)[0]:
        return False
    if buscar_espacio_por_id(id_espacio, conexion, cursor) is None:
        return False
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
    if not validar_entero_positivo(id_espacio)[0]:
        return None
    if buscar_espacio_por_id(id_espacio, conexion, cursor) is None:
        return None
    cursor.execute("""
        SELECT *
        FROM espacio
        WHERE id_espacio=%s
    """, (id_espacio,))

    return cursor.fetchone()