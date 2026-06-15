def crear_disciplina(nombre, conexion, cursor):

    cursor.execute("""
        INSERT INTO disciplina(nombre)
        VALUES(%s)
    """,(nombre,))

    conexion.commit()

    print("Disciplina creada")

def buscar_disciplina_por_id(id_disciplina, conexion, cursor):
    return None

def listar_disciplinas(conexion, cursor):

    cursor.execute("""
        SELECT *
        FROM disciplina
    """)

    for fila in cursor.fetchall():
        print(fila)


def modificar_disciplina(id_disciplina, nombre, conexion, cursor):

    cursor.execute("""
        UPDATE disciplina
        SET nombre=%s
        WHERE id_disciplina=%s
    """, (nombre, id_disciplina))

    conexion.commit()

    print("Disciplina actualizada")


def eliminar_disciplina(id_disciplina, conexion, cursor):
    try:
        cursor.execute(
            "DELETE FROM disciplina WHERE id_disciplina=%s",
            (id_disciplina,)
        )
        conexion.commit()
        return True
    except Exception as e:
        return False
