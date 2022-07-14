from flask import request, redirect, render_template
from flask_login import login_required
from . import datos, controller

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
        elif(btnvalor == 'editar'):
            controller.modificar_dato(request)
    except Exception :  #falta perfecionar esa pagina de errores 
        error  = 'Solicitud imcopleta, Faltan Datos '
        ruta   = 'proveedores'
        btn    = 'Volver a la lista de Proveedores '
        return render_template('Errores.html',erro=error,rut=ruta,btn=btn)
    return redirect('datos')

@datos.route('/modificar-dato', methods=['GET','POST'])
@login_required
def modificar_dato():
    id          = request.args.get('id')
    data        = controller.obtener_dato(id)
    btn         = 'editar'
    btn_text    = 'Guardar Dato'
    textofor    = 'Modificar Dato'
    return render_template('RegDato.html',
            pro = data, btn = btn, texto = textofor, btntext = btn_text)

@datos.route('/eliminar-dato', methods=['GET','POST'])
@login_required
def eliminar_dato():
    controller.eliminar_dato(request)
    return redirect('datos')


@datos.route('/registrar-dato', methods=['GET', 'POST'])
@login_required
def registrar_dato(): 
    btn        = 'Nuevo'
    btn_text   = 'Guardar Dato '
    textofor   = 'Registrar Dato'
    data       = ['']
    return render_template('RegDato.html',
            pro = data, btn = btn, texto = textofor, btntext = btn_text)
