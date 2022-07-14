 USE datos;
 GO
-- stp insertar
 CREATE PROCEDURE stp_insertarDato
 (
 @texto       VARCHAR(50),
 @descripcion VARCHAR(120)
 )
 AS
 BEGIN
     SET NOCOUNT ON;  
   
		INSERT INTO datos (texto, descripcion)
			VALUES (@texto, @descripcion);
END 
GO
-- stp Modificar
 CREATE PROCEDURE stp_modificarDato
 (
 @id		  INT,
 @texto       VARCHAR(50),
 @descripcion VARCHAR(120)
 )
 AS 
BEGIN 
IF EXISTS (SELECT id FROM datos WHERE id = @id)
  BEGIN
			UPDATE datos SET
				   texto		= @texto,
                   descripcion  = @descripcion
			WHERE  id           = @id;
  END
END
GO
-- stp Eliminar
 CREATE PROCEDURE stp_eliminarDato 
 (
 @id		  INT
 )
 AS 
BEGIN 
IF EXISTS (SELECT id FROM datos WHERE id = @id)
  BEGIN
		DELETE FROM datos WHERE id = @id;
  END
END
GO
-- stp mostrar Datos
 CREATE PROCEDURE stp_mostrarDatos
(
 @id INT
)
AS
BEGIN
    
		SELECT id,texto,descripcion FROM datos
			WHERE id = @id;

END
GO
EXECUTE stp_mostrarDatos 1 ;
INSERT INTO datos(texto, descripcion) 
        VALUES('Godzilla', 'Dinosaurio radiactivo protector de Tokio.'),
              ('Poletergeish','Fantasmas que estan atrapados en la realidad.'),
              ('Valiente','Historia de lazos rotos y restaurados.'),
              ('Dark','Relato de la paradoja del tiempo y espacio');
GO
