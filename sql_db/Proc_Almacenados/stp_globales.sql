/*
 * Scripts que trabajan con varias tablas a la vez
 * stp mostrar una tabla -> stp_mostrarRegistros
 *				-- datos
 * 				-- usuarios
 */
 
 -- Muestra todos los registros de cualquier tabla

CREATE PROCEDURE stp_mostrarRegistros
(
@tabla   VARCHAR(50)
)
AS
BEGIN
SET NOCOUNT ON;
 

	IF(@tabla = 'usuarios')
	   SELECT cedula, nombre,rol, estado FROM usuarios
	ELSE IF (@tabla = 'datos')
       SELECT id, texto, descripcion FROM datos
    
END
GO
EXECUTE stp_mostrarRegistros 'usuarios'