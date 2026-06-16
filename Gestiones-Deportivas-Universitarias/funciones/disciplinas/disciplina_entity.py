from funciones.validaciones import validar_no_vacio, validar_entero_positivo


def crear_disciplina(nombre, conexion, cursor):
    if not validar_no_vacio(nombre)[0]:
        return False
    cursor.execute("""
        INSERT INTO disciplina(nombre)
        VALUES(%s)
    """,(nombre,))

    conexion.commit()


def buscar_disciplina_por_id(id_disciplina, conexion, cursor):
    if not validar_entero_positivo(id_disciplina)[0]:
        return None
    cursor.execute("""
        SELECT *
        FROM disciplina
        WHERE id_disciplina=%s
    """, (id_disciplina,))

    return cursor.fetchone()

def listar_disciplinas(conexion, cursor):

    cursor.execute("""
        SELECT *
        FROM disciplina
    """)
    return cursor.fetchall()
    

def modificar_disciplina(id_disciplina, nombre, conexion, cursor):
    if not validar_entero_positivo(id_disciplina)[0]:
        return False
    if buscar_disciplina_por_id(id_disciplina, conexion, cursor) is None:
        return False
    if not validar_no_vacio(nombre)[0]:
        return False
        
    cursor.execute("""
        UPDATE disciplina
        SET nombre=%s
        WHERE id_disciplina=%s
    """, (nombre, id_disciplina))

    conexion.commit()



def eliminar_disciplina(id_disciplina, conexion, cursor):
    if not validar_entero_positivo(id_disciplina)[0]:
        return False
    if buscar_disciplina_por_id(id_disciplina, conexion, cursor) is None:
        return False
    try:
        cursor.execute(
            "DELETE FROM disciplina WHERE id_disciplina=%s",
            (id_disciplina,)
        )
        conexion.commit()
        return True
    except Exception as e:
        return False
