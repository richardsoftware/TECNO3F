-- PROYECTO ACADEMIAS

-- CREAR LA BASE DE DATOS
CREATE DATABASE institucion_educativa;

-- nos paramos en la bbdd creada
USE institucion_educativa;

/* CREAR LAS ENTIDADES O TABLAS DEL PROYECTO

 TABLA ESPECIALIDAD */

-- ************************************** Academias
CREATE TABLE IF NOT EXISTS Academias(
 id_academia int NOT NULL PRIMARY KEY AUTO_INCREMENT,
 nombre      varchar(50) NOT NULL,
 Tel         varchar(50) NOT NULL,
 Web         varchar(50) NOT NULL,

);

-- ************************************** Profesores
CREATE TABLE Profesores
(
 id_profesor int NOT NULL PRIMARY KEY AUTO_INCREMENT,
 nombre      varchar(50) NOT NULL,
 apellido    varchar(50) NOT NULL,
 mail        mail VARCHAR(255) UNIQUE,
 telefono    varchar(50) NOT NULL,
 id_academia int NOT NULL,

 FOREIGN KEY ( id_academia ) REFERENCES Academias ( id_academia )
);
-- ************************************** Alumnos
CREATE TABLE Alumnos
(
 id_alumno   int NOT NULL PRIMARY KEY AUTO_INCREMENT,
 nombre      varchar(50) NOT NULL,
 apellido    varchar(50) NOT NULL,
 mail        varchar(50) NOT NULL,
 telefono    varchar(50) NOT NULL,
 id_academia int NOT NULL,

 FOREIGN KEY ( id_academia ) REFERENCES Academias ( id_academia )
);

-- ************************************** Cursos
CREATE TABLE Cursos
(
 id_curso    int NOT NULL PRIMARY KEY AUTO_INCREMENT,
 nombre      varchar(50) NOT NULL,
 descripcion text NOT NULL,
 id_profesor int NOT NULL,

 FOREIGN KEY ( id_profesor ) REFERENCES Profesores ( id_profesor )
);
-- ************************************** Alumnos_x_cursos
CREATE TABLE Alumnos_x_cursos
(
 id        int NOT NULL PRIMARY KEY AUTO_INCREMENT,
 id_alumno int NOT NULL,
 id_curso  int NOT NULL,

 FOREIGN KEY ( id_alumno ) REFERENCES Alumnos ( id_alumno ),
 FOREIGN KEY ( id_curso ) REFERENCES Cursos ( id_curso )
);
-- ************************************** Notas
CREATE TABLE Notas
(
 id_nota   int NOT NULL PRIMARY KEY AUTO_INCREMENT,
 nota      float NOT NULL,
 id_alumno int NOT NULL,
 id_curso  int NOT NULL,

 FOREIGN KEY ( id_alumno ) REFERENCES Alumnos ( id_alumno ),
 FOREIGN KEY ( id_curso ) REFERENCES Cursos ( id_curso )
);
