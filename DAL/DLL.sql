CREATE TABLE empleados (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(255) NOT NULL,
    telefono VARCHAR(15),
    email VARCHAR(100) UNIQUE,
    fecha_inicio DATE NOT NULL,
    salario DECIMAL(10, 2) NOT NULL,
    tipo ENUM('Administrador', 'Empleado Regular') NOT NULL
);

CREATE TABLE departamentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) UNIQUE NOT NULL,
    descripcion TEXT,
    gerente INT,
    FOREIGN KEY (gerente) REFERENCES empleados(id) ON DELETE SET NULL
);

CREATE TABLE proyectos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE
);

CREATE TABLE registrotiempo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATE NOT NULL,
    horas_trabajadas DECIMAL(5, 2) NOT NULL,
    descripcion TEXT,
    empleado_id INT NOT NULL,
    proyecto_id INT NOT NULL,
    FOREIGN KEY (empleado_id) REFERENCES empleados(id) ON DELETE CASCADE,
    FOREIGN KEY (proyecto_id) REFERENCES proyectos(id) ON DELETE CASCADE
);

CREATE TABLE informes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tipo_informe VARCHAR(50) NOT NULL,
    fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    empleado_id INT,
    departamento_id INT,
    proyecto_id INT,
    FOREIGN KEY (empleado_id) REFERENCES empleados(id) ON DELETE SET NULL,
    FOREIGN KEY (departamento_id) REFERENCES departamentos(id) ON DELETE SET NULL,
    FOREIGN KEY (proyecto_id) REFERENCES proyectos(id) ON DELETE SET NULL
);

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    rol_id INT,
    FOREIGN KEY (rol_id) REFERENCES roles(id) ON DELETE SET NULL
);

CREATE TABLE roles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) UNIQUE NOT NULL,
    descripcion TEXT
);
