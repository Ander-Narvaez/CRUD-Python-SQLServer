/*
 * Script de la tabla Usuarios
 * stp de insertar		     -> pa_insertarUsuario
 * stp de cambiar estado	 -> pa_modificarUsario
 * stp de modificar 		 -> pa_cambiarEstadoUsuario
 * stp de mostrar un usuario -> pa_mostrarUsuarios
 */

-- spt de insertar
CREATE PROCEDURE stp_insertarUsuario
(
@cedula 	VARCHAR(50),
@nombre 	VARCHAR(45),
@rol   	    VARCHAR(50),
@contra     VARCHAR(MAX),
@estado 	VARCHAR(10)
)
AS
BEGIN
		
         INSERT INTO usuarios(cedula,nombre,rol,contra,estado)
			VALUES (@cedula, @nombre, @rol, @contra, @estado);     
END 
GO
-- stp de modificar 
CREATE PROCEDURE stp_modificarUsuario
(
@cedula 	VARCHAR(50),
@nombre 	VARCHAR(45),
@rol   	    VARCHAR(50),
@contra     VARCHAR(MAX),
@estado 	VARCHAR(10)

)
AS
BEGIN
	IF EXISTS (SELECT cedula FROM usuarios WHERE cedula = @cedula)
       BEGIN
		UPDATE usuarios SET
			   nombre      = @nombre,
               rol         = @rol,
               contra      = @contra,
               estado 	   = @estado
		WHERE  cedula      = @cedula;
           
       END
END
GO
-- stp de cambiar el estado
CREATE PROCEDURE stp_cambiarEstadoUsuario
(
@cedula     VARCHAR(50)
)
AS
BEGIN
DECLARE @estadoActual VARCHAR(10);

		IF EXISTS (SELECT cedula FROM usuarios WHERE cedula = @cedula)
		 BEGIN	
			SET @estadoActual = (SELECT estado FROM usuarios WHERE cedula = @cedula);
            
            IF (@estadoActual = 'Activo')            
				SET @estadoActual = 'Inactivo';               
            ELSE            
				SET @estadoActual = 'Activo';       
          END

            UPDATE usuarios SET estado = @estadoActual WHERE cedula = @cedula;
END
GO
-- stp de mostrar un cliente
CREATE PROCEDURE stp_mostrarUsuarios
(
@cedula     VARCHAR(50)
)
AS
BEGIN
	IF ((SELECT COUNT(cedula) FROM usuarios WHERE cedula = @cedula) > 0)
    
		SELECT cedula, nombre, rol, estado FROM usuarios WHERE cedula = @cedula;

END 

