def crear_disciplina(nombre, conexion, cursor):

    cursor.execute("""
        INSERT INTO disciplina(nombre)
        VALUES(%s)
    """,(nombre,))

    conexion.commit()

    print("Disciplina creada")

    cursor.close()
    conexion.close()


def listar_disciplinas(conexion, cursor):

    cursor.execute("""
        SELECT *
        FROM disciplina
    """)

    for fila in cursor.fetchall():
        print(fila)

    cursor.close()
    conexion.close()