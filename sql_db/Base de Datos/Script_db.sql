
 CREATE DATABASE datos;
 GO
 USE datos;
 GO
 -- -----------------------------------------------------
-- Table dbo.datos
-- -----------------------------------------------------
 CREATE TABLE datos 
 (
 id          SMALLINT     NOT NULL IDENTITY(1,1),
 texto       VARCHAR(50)  NOT NULL,
 descripcion VARCHAR(120) NOT NULL,

 CONSTRAINT PK_id PRIMARY KEY CLUSTERED (id)
 );
GO
-- -----------------------------------------------------
-- Table dbo.usuarios
-- -----------------------------------------------------
CREATE TABLE usuarios
(
   cedula INT 	        NOT NULL,
   nombre VARCHAR(50)   NOT NULL,
   rol    VARCHAR(45)   NOT NULL DEFAULT 'Invitado',
   contra VARCHAR(MAX)  NOT NULL,
   estado VARCHAR(25)   NOT NULL DEFAULT 'Activo',
  
  PRIMARY KEY  CLUSTERED (cedula),
  CONSTRAINT chk_rolUser CHECK (rol = 'Administrador' OR rol = 'Invitado'),
  CONSTRAINT chk_estadoUser CHECK (estado = 'Activo' OR estado = 'Inactivo')
);
GO

insert into usuarios (cedula,nombre,rol,contra,estado) 
       values(207980615,'Ander','Administrador','1q2w3e4r','Activo')