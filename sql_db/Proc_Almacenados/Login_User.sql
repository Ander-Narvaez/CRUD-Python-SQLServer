/*
 * Script de la tabla Trabajador, donde valida el login
 * stp de recibe los datos CEDULA, CONTRASEÑA
 * Verifica si existe algún registro.
 *	SI: Retorna los datos del usuario
 *	NO: Retorna falso 
 */

CREATE PROCEDURE pa_login
(
@pcedula INT,
@pcontrasena VARCHAR(MAX)
)
AS
BEGIN

	IF EXISTS (SELECT cedula FROM usuarios WHERE contra = @pcontrasena AND cedula = @pcedula)
		
        SELECT cedula, nombre, rol FROM usuarios 
			   WHERE contra = @pcontrasena AND cedula = @pcedula;

END