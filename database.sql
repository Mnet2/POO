-- 1. Creación de la Base de Datos
CREATE DATABASE IF NOT EXISTS ecotech_db;
USE ecotech_db;

-- ==========================================
-- 2. Creación de Tablas Principales
-- ==========================================

-- Tabla DEPARTAMENTOS
-- Atributos según UML: id, nombre. 
-- El campo 'gerente_id' se deja NULL inicialmente para evitar conflictos de creación
-- (problema del huevo y la gallina con la tabla Empleados).
CREATE TABLE IF NOT EXISTS departamentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    gerente_id INT NULL 
) ENGINE=InnoDB;

-- Tabla EMPLEADOS
-- Atributos según UML: id, nombre, direccion, telefono, correo, fecha_contrato, salario, departamento.
CREATE TABLE IF NOT EXISTS empleados (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(200),
    telefono VARCHAR(20),
    correo VARCHAR(100) UNIQUE NOT NULL,
    fecha_contrato DATE NOT NULL,
    salario INT NOT NULL,
    departamento_id INT,
    CONSTRAINT fk_empleado_departamento
        FOREIGN KEY (departamento_id) REFERENCES departamentos(id)
        ON DELETE SET NULL
) ENGINE=InnoDB;

-- RELACIÓN CIRCULAR: Departamento -> tiene un -> Gerente (Empleado)
-- Ahora que la tabla 'empleados' existe, conectamos la llave foránea del gerente.
ALTER TABLE departamentos
ADD CONSTRAINT fk_departamento_gerente
FOREIGN KEY (gerente_id) REFERENCES empleados(id)
ON DELETE SET NULL;

-- Tabla PROYECTOS
-- Atributos según UML: id, nombre, descripcion, fecha_inicio.
-- Incluye 'director_id' para relacionarlo con un Empleado jefe del proyecto.
CREATE TABLE IF NOT EXISTS proyectos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    fecha_inicio DATE NOT NULL,
    director_id INT,
    CONSTRAINT fk_proyecto_director
        FOREIGN KEY (director_id) REFERENCES empleados(id)
        ON DELETE SET NULL
) ENGINE=InnoDB;

-- ==========================================
-- 3. Tablas de Relación (Muchos a Muchos)
-- ==========================================

-- Tabla PROYECTO_PARTICIPANTES
-- Resuelve la relación de que un proyecto tiene muchos empleados participantes (1..*)
CREATE TABLE IF NOT EXISTS proyecto_participantes (
    proyecto_id INT NOT NULL,
    empleado_id INT NOT NULL,
    PRIMARY KEY (proyecto_id, empleado_id),
    CONSTRAINT fk_part_proyecto
        FOREIGN KEY (proyecto_id) REFERENCES proyectos(id)
        ON DELETE CASCADE,
    CONSTRAINT fk_part_empleado
        FOREIGN KEY (empleado_id) REFERENCES empleados(id)
        ON DELETE CASCADE
) ENGINE=InnoDB;

-- Tabla REGISTRO_TIEMPO
-- Requisito funcional para registrar las horas trabajadas por empleado en un proyecto.
CREATE TABLE IF NOT EXISTS registro_tiempo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    empleado_id INT NOT NULL,
    proyecto_id INT NOT NULL,
    fecha DATE NOT NULL,
    horas INT NOT NULL,
    descripcion_tarea VARCHAR(255),
    CONSTRAINT fk_tiempo_empleado
        FOREIGN KEY (empleado_id) REFERENCES empleados(id),
    CONSTRAINT fk_tiempo_proyecto
        FOREIGN KEY (proyecto_id) REFERENCES proyectos(id)
) ENGINE=InnoDB;