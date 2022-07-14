from flask import request, redirect, render_template, url_for
from flask_login import login_required
from . import datos, controller



# ------------------------ Raiz ------------------------
@datos.route("/", methods=["GET", "POST"])
def index():
    datos = controller.mostrar_datos()
    return redirect(url_for("Datos.html"), values=datos)

@datos.route('/datos', methods=['GET', 'POST'])
@login_required
def mostrar_datos(): 
    datos = controller.mostrar_datos()
    return render_template('Datos.html', values=datos)


@datos.route('/guardar-dato', methods=['GET', 'POST'])
@login_required
def guardar_dato():
    try:
        btnvalor = request.form['btnpro']
        if(btnvalor == 'Nuevo'):
            controller.guardar_dato(request)
        elif(btnvalor=='editar'):
            controller.modificar_dato(request)
    except Exception :  #falta perfecionar esa pagina de errores 
        error  = 'Solicitud imcopleta, Faltan Datos '
        ruta   = 'datos'
        btn    = 'Volver a la lista de Datos'
        return render_template('Errores.html',erro=error,rut=ruta,btn=btn)
    return redirect('datos')

@datos.route('/modificar-dato', methods=['GET','POST'])
@login_required
def modificar_dato():
    idproveedor = request.args.get('id')
    data        = controller.obtener_dato(idproveedor)
    btn         = 'editar'
    btn_text    = 'Guardar Dato'
    textofor    = 'Modificar Dato'
    return render_template('RegDato.html',
            pro = data, btn = btn, texto = textofor, btntext = btn_text)


@datos.route('/registrar-dato', methods=['GET', 'POST'])
@login_required
def registrar_dato(): 
    btn        = 'Nuevo'
    btn_text   = 'Guardar Dato '
    textofor   = 'Registrar Dato'
    data       = ['']
    return render_template('RegDato.html',
            pro = data, btn = btn, texto = textofor, btntext = btn_text)
