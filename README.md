# Sistema-BD1
Aqui se encuentran las creaciones de tablas, inserts, datos maestros y consultas resueltas.

# Tablas
CREATE DATABASE actividades_deportivas;

USE actividades_deportivas;

CREATE TABLE estudiante (
    id_estudiante INT AUTO_INCREMENT PRIMARY KEY,
    documento VARCHAR(20) NOT NULL UNIQUE,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    correo VARCHAR(100) NOT NULL UNIQUE,
    carrera VARCHAR(100) NOT NULL,
    facultad VARCHAR(100) NOT NULL
);

CREATE TABLE disciplina (
    id_disciplina INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE espacio (
    id_espacio INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    ubicacion VARCHAR(150)
);

CREATE TABLE actividad (
    id_actividad INT AUTO_INCREMENT PRIMARY KEY, 
    nombre VARCHAR(100) NOT NULL,
    id_disciplina INT NOT NULL,
    id_espacio INT NOT NULL,
    cupo_maximo INT NOT NULL,
    dia VARCHAR(20) NOT NULL,
    horario TIME NOT NULL,
    estado ENUM(
        'ABIERTA',
        'CERRADA',
        'FINALIZADA',
        'CANCELADA'
    ) NOT NULL DEFAULT 'ABIERTA',
    FOREIGN KEY (id_disciplina)
        REFERENCES disciplina(id_disciplina),
    FOREIGN KEY (id_espacio)
        REFERENCES espacio(id_espacio),
    CHECK (cupo_maximo > 0)
);

CREATE TABLE inscripcion (
    id_inscripcion INT AUTO_INCREMENT PRIMARY KEY,
    id_estudiante INT NOT NULL,
    id_actividad INT NOT NULL,
    fecha_inscripcion DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    estado ENUM(
        'CONFIRMADA',
        'ESPERA'
    ) NOT NULL,
    FOREIGN KEY (id_estudiante)
        REFERENCES estudiante(id_estudiante),
    FOREIGN KEY (id_actividad)
        REFERENCES actividad(id_actividad),
    UNIQUE(id_estudiante, id_actividad)
);

CREATE TABLE asistencia (
    id_asistencia INT AUTO_INCREMENT PRIMARY KEY,
    id_inscripcion INT NOT NULL,
    fecha DATE NOT NULL,
    asistio BOOLEAN NOT NULL,
    FOREIGN KEY (id_inscripcion)
        REFERENCES inscripcion(id_inscripcion),
    UNIQUE(id_inscripcion, fecha)

# Inserts
INSERT INTO estudiante
(documento,nombre,apellido,correo,carrera,facultad)
VALUES

('50000001',
'Juan',
'Pérez',
'juan@universidad.edu',
'Ingeniería en Sistemas',
'Ingeniería'),

('50000002',
'María',
'Rodríguez',
'maria@universidad.edu',
'Contador Público',
'Ciencias Económicas'),

('50000003',
'Lucía',
'Gómez',
'lucia@universidad.edu',
'Ingeniería en Sistemas',
'Ingeniería');

INSERT INTO actividad
(
nombre,
id_disciplina,
id_espacio,
cupo_maximo,
dia,
horario,
estado
)
VALUES

(
'Fútbol Recreativo Mixto',
1,
1,
30,
'Lunes',
'18:00:00',
'ABIERTA'
),

(
'Atletismo Inicial',
3,
4,
20,
'Martes',
'19:00:00',
'ABIERTA'
),

(
'Funcional Turno Mañana',
6,
3,
15,
'Miércoles',
'08:00:00',
'ABIERTA'
);

INSERT INTO inscripcion
(
id_estudiante,
id_actividad,
estado
)
VALUES

(1,1,'CONFIRMADA'),
(2,1,'CONFIRMADA'),
(3,1,'ESPERA'),
(1,2,'CONFIRMADA');

INSERT INTO asistencia
(
id_inscripcion,
fecha,
asistio
)
VALUES

(1,'2026-06-01',TRUE),
(2,'2026-06-01',FALSE),
(4,'2026-06-02',TRUE);

# Datos Maestros
INSERT INTO disciplina(nombre)
VALUES
('Fútbol'),
('Básquetbol'),
('Atletismo'),
('Vóleibol'),
('Yoga'),
('Funcional'),
('Gimnasio');

INSERT INTO espacio(nombre, ubicacion)
VALUES
('Cancha Principal', 'Campus Norte'),
('Cancha Auxiliar', 'Campus Norte'),
('Gimnasio Central', 'Campus Sur'),
('Pista de Atletismo', 'Campus Este'),
('Sala Multiuso', 'Campus Central');

# Consultas
# 1: 
SELECT
    a.id_actividad,
    a.nombre,
    COUNT(i.id_inscripcion) AS cantidad_confirmados
FROM actividad a
LEFT JOIN inscripcion i
    ON a.id_actividad = i.id_actividad
    AND i.estado = 'CONFIRMADA'
GROUP BY a.id_actividad, a.nombre
ORDER BY cantidad_confirmados DESC;

# 2:
SELECT
    a.id_actividad,
    a.nombre,
    a.cupo_maximo,
    COUNT(i.id_inscripcion) AS confirmados,
    a.cupo_maximo - COUNT(i.id_inscripcion) AS cupos_disponibles
FROM actividad a
LEFT JOIN inscripcion i
    ON a.id_actividad = i.id_actividad
    AND i.estado = 'CONFIRMADA'
GROUP BY a.id_actividad, a.nombre, a.cupo_maximo
HAVING cupos_disponibles > 0;

# 3:
SELECT
    d.nombre AS disciplina,
    COUNT(i.id_inscripcion) AS cantidad_inscriptos
FROM disciplina d
JOIN actividad a
    ON d.id_disciplina = a.id_disciplina
LEFT JOIN inscripcion i
    ON a.id_actividad = i.id_actividad
    AND i.estado = 'CONFIRMADA'
GROUP BY d.id_disciplina, d.nombre
ORDER BY cantidad_inscriptos DESC;

# 4:
SELECT
    e.carrera,
    COUNT(i.id_inscripcion) AS cantidad_inscriptos
FROM estudiante e
JOIN inscripcion i
    ON e.id_estudiante = i.id_estudiante
WHERE i.estado = 'CONFIRMADA'
GROUP BY e.carrera
ORDER BY cantidad_inscriptos DESC;

SELECT
    e.facultad,
    COUNT(i.id_inscripcion) AS cantidad_inscriptos
FROM estudiante e
JOIN inscripcion i
    ON e.id_estudiante = i.id_estudiante
WHERE i.estado = 'CONFIRMADA'
GROUP BY e.facultad
ORDER BY cantidad_inscriptos DESC;

# 5:
SELECT
    a.id_actividad,
    a.nombre,
    ROUND(
        (COUNT(i.id_inscripcion) * 100.0) /
        a.cupo_maximo,
        2
    ) AS porcentaje_ocupacion
FROM actividad a
LEFT JOIN inscripcion i
    ON a.id_actividad = i.id_actividad
    AND i.estado = 'CONFIRMADA'
GROUP BY
    a.id_actividad,
    a.nombre,
    a.cupo_maximo;

# 6:
SELECT
    ac.nombre,
    ROUND(
        SUM(CASE WHEN a.asistio = TRUE THEN 1 ELSE 0 END)
        * 100.0 /
        COUNT(*),
        2
    ) AS porcentaje_asistencia
FROM actividad ac
JOIN inscripcion i
    ON ac.id_actividad = i.id_actividad
JOIN asistencia a
    ON i.id_inscripcion = a.id_inscripcion
GROUP BY ac.id_actividad, ac.nombre;

# 7:
SELECT
    e.id_estudiante,
    e.nombre,
    e.apellido,
    COUNT(*) AS faltas
FROM estudiante e
JOIN inscripcion i
    ON e.id_estudiante = i.id_estudiante
JOIN asistencia a
    ON i.id_inscripcion = a.id_inscripcion
WHERE a.asistio = FALSE
GROUP BY
    e.id_estudiante,
    e.nombre,
    e.apellido
HAVING COUNT(*) >= 3;

# 8:
# Estudiantes en lista de espera:
SELECT
    e.nombre,
    e.apellido,
    a.nombre AS actividad
FROM estudiante e
JOIN inscripcion i
    ON e.id_estudiante = i.id_estudiante
JOIN actividad a
    ON i.id_actividad = a.id_actividad
WHERE i.estado = 'ESPERA';

# Actividades canceladas o finalizadas:
SELECT
    nombre,
    estado
FROM actividad
WHERE estado IN ('CANCELADA', 'FINALIZADA');

# Top 5 estudiantes con más asistencias:
SELECT
    e.nombre,
    e.apellido,
    COUNT(*) AS asistencias
FROM estudiante e
JOIN inscripcion i
    ON e.id_estudiante = i.id_estudiante
JOIN asistencia a
    ON i.id_inscripcion = a.id_inscripcion
WHERE a.asistio = TRUE
GROUP BY
    e.id_estudiante,
    e.nombre,
    e.apellido
ORDER BY asistencias DESC
LIMIT 5;
