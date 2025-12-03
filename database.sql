-- Creación de la Base de Datos
CREATE DATABASE IF NOT EXISTS ecotech_db;
USE ecotech_db;


-- Tablas Principales

-- Tabla DEPARTAMENTOS
CREATE TABLE IF NOT EXISTS departamentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    gerente_id INT NULL 
) ENGINE=InnoDB;

-- Tabla EMPLEADOS
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

ALTER TABLE departamentos
ADD CONSTRAINT fk_departamento_gerente
FOREIGN KEY (gerente_id) REFERENCES empleados(id)
ON DELETE SET NULL;

-- Tabla PROYECTOS
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

-- Tabla PROYECTO_PARTICIPANTES
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

USE ecotech_db;

CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL, -- Aquí guardaremos el HASH, no la clave real
    rol VARCHAR(20) DEFAULT 'user'  -- Roles: 'admin', 'user', 'invitado'
);