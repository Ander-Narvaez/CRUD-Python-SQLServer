from app.database.ConexionDB import SQL
from werkzeug.security import generate_password_hash

def guardar_usuario(request):
    """
        Recibe los datos del usuario a registrar.
    """
    if (request.method == "POST"):
        nombre  = request.form['nombre']
        contra  = request.form['contra1']
        contra2 = request.form['contra2']
        cedula  = request.form['cedula']
        rol     = request.form['rol']
        estado  = request.form['estado']
        # Valida la contraseña, falta codificar la contraseña
        if contra == contra2 and contra != '':
            conexion = SQL()
            conexion.execute_procedure("stp_insertarUsuario ?,?,?,?,? ", [cedula, nombre, rol,generate_password_hash(contra2, method='sha256'),estado])


def modificar_usuario(request):
    """
        Recibe los datos del usuario a modificar.
        - A pesar de recibir la cédula, esta no se modifica.
    """
    if (request.method == "POST"):
        nombre  = request.form['nombre']
        contra  = request.form['contra1']
        contra2 = request.form['contra2']
        cedula  = request.form['cedula']
        rol     = request.form['rol']
        estado  = request.form['estado']
        # Valida la contraseña, falta codificar la contraseña
        if contra == contra2 and contra != '':
            conexion  = SQL()
            conexion.execute_procedure("stp_modificarUsuario ?,?,?,?,? ", [cedula, nombre, rol,contra2,estado])


def cambiar_estado(cedula):
    """
        Cambia el estado de un usuario con la cédula enviada.
    """
    conexion  = SQL()
    conexion.execute_procedure("stp_cambiarEstadoUsuario ? ", [cedula])
         
 
def obtener_usuario(cedula):
    """
        Se recibe la cédula de un usuario, para identificarlo y retornar sus datos obtenidos desde la BD.
        - La cédula es de tipo int.
    """  
    if cedula != None and cedula != '' and cedula != 0:
        conexion  = SQL()
        datos     = conexion.call_store_procedure_return("stp_mostrarUsuarios ? ", [cedula])
        return datos
    return None


def mostrar_usuarios():
    """
        Obtiene y retorna todos los usuarios registrados en la BD.
    """
    conexion   = SQL()
    usuarios = 'usuarios'
    datos      = conexion.call_store_procedure_return("stp_mostrarRegistros ? ", [usuarios])
    return datos