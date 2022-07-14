from app.database.ConexionDB import SQL

def guardar_dato(request):
    """
        Guarda un nuevo dato en la BD.
    """
    if (request.method == 'POST'):
        texto       = request.form['Texto'] 
        descripcion = request.form['Descripcion']
        print(texto,descripcion)
        conexion    = SQL()
        conexion.execute_procedure("stp_insertarDato ?,? ", [texto, descripcion])

def modificar_dato(request):
    """
        Se actualiza los datos, de acuerdo al ID auto incrementable.
        - El id se recibe por el método get y los demás datos por el método POST.
    """
    id_dato = request.args.get("id")
    if (request.method == 'POST' and id_dato != ''):
        texto       = request.form['Texto'] 
        descripcion = request.form['Descripcion']
        conexion = SQL()
        conexion.execute_procedure("stp_modificarDato ?,?,? ", [id_dato, texto, descripcion])


def obtener_dato(id_dato):
    """
        Identifica por medio del ID y retorna los datos de un proveedor registrado en la BD.
        - El ID es de tipo int.
    """
    if (id != ''):
        conexion = SQL()
        datos    = conexion.call_store_procedure_return("stp_mostrarDatos ? ", [id_dato])
        return datos
    return None

def mostrar_datos():
    """
        Extrae todos los proveedores registrados en la BD.
    """
    conexion = SQL()
    datos    = conexion.call_store_procedure_return("stp_mostrarRegistros ? ", ['datos'])
    return datos

def eliminar_dato(request):
    id_dato = request.args.get("id")
    conexion = SQL()
    datos    = conexion.execute_procedure("stp_eliminarDato ? ", [id_dato])
    return datos