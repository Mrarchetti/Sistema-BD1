def crear_estudiante(
    documento,
    nombre,
    apellido,
    correo,
    carrera,
    facultad,
    conexion,
    cursor
):

    sql = """
    INSERT INTO estudiante
    (documento,nombre,apellido,correo,carrera,facultad)
    VALUES (%s,%s,%s,%s,%s,%s)
    """

    cursor.execute(sql,(
        documento,
        nombre,
        apellido,
        correo,
        carrera,
        facultad
    ))

    conexion.commit()

    print("Estudiante creado")


def listar_estudiantes(conexion, cursor):


    cursor.execute("SELECT * FROM estudiante")

    resultados = cursor.fetchall()

    for fila in resultados:
        print(fila)


def buscar_estudiante_por_documento(documento, conexion, cursor):

    cursor.execute(
        "SELECT * FROM estudiante WHERE documento=%s",
        (documento,)
    )

    return cursor.fetchone()


def modificar_estudiante(
    id_estudiante,
    documento,
    nombre,
    apellido,
    correo,
    carrera,
    facultad,
    conexion,
    cursor
):


    cursor.execute("""
        UPDATE estudiante
        SET documento=%s,
            nombre=%s,
            apellido=%s,
            correo=%s,
            carrera=%s,
            facultad=%s
        WHERE id_estudiante=%s
    """,(
        documento,
        nombre,
        apellido,
        correo,
        carrera,
        facultad,
        id_estudiante
    ))

    conexion.commit()

    print("Estudiante actualizado")



def eliminar_estudiante(id_estudiante, conexion, cursor):

    try:
        cursor.execute(
        "DELETE FROM estudiante WHERE id_estudiante=%s",
        (id_estudiante,)
        )

        conexion.commit()

    except Exception as e:
        return False

    return True
#Retornamos True si fue exitosa la eliminacion, false en caso contrario