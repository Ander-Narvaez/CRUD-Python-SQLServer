from app.datos import dato
from app.datos.dato import Dato
from app.database.ConexionDB import Sql

def insert_dato(request):
    if (request.method == "POST"):
        ptexto       = request.form['txtTexto'] 
        pdescripcion = request.form['txtDescrip']

        print("Registrando dato...")
        dato = Dato(None, ptexto, pdescripcion)
        actions = Sql()
        actions.execute_procedure("stp_insertarDato",dato.get_list_insert_db())

def update_dato(request):
    if (request.method == "POST"):
        pId   = request.form["id_repuesto"]
        ptexto       = request.form['txtTexto'] 
        pdescripcion = request.form['txtDescrip']
        print("Actualizando repueso...")
        dato = Dato(pId,  ptexto, pdescripcion)
        actions = Sql()
        actions.execute_procedure("stp_modificarDato",dato.get_list_update_db())

def delete_dato(request):
    pId_repuesto = request.args.get("id")
    print("Eliminando repuesto...")
    actions = Sql()
    actions.execute_procedure("stp_eliminarDato",[pId_repuesto])

def mostrar_datos(request):
    print("Extrayendo modelos...")
    actions = Sql()
    datos = []
    id = request.args.get("id")
    if id == None:
        datos = actions.call_store_procedure_return("stp_mostrarDatos",[])
    else:
        datos = actions.call_store_procedure_return("stp_mostrarDatos",[id])
    repuestos = []
    for dato_actual in datos:
        dato_nuevo = Dato(dato_actual[0], dato_actual[1], dato_actual[2],
                                  dato_actual[3], dato_actual[4])
        repuestos.append(dato_nuevo)
    return repuestos