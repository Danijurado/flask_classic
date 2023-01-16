from registro_ig import app
from flask import render_template, request, redirect, url_for,flash
from registro_ig.models import *
from datetime import date,datetime
from registro_ig.forms import MovementsForm

def validateForm(requestForm):
    hoy = date.today().isoformat()
    errores=[]
    if requestForm['date'] > hoy:
        errores.append("fecha invalida: La fecha introducida es a futuro")
    if requestForm['concept'] == "":
        errores.append("concepto vacio: Introduce un concepto para el registro")
    if requestForm['quantity'] == "" or float(requestForm['quantity']) == 0.0:
        errores.append("cantidad vacio o cero: Introduce una cantidad positiva o negativa")   
    return errores

@app.route('/')
def index():
    
    registros = select_all()
    
    datos_mov=[
        {"id":1,"date":"2022-01-01","concept":"Sueldo","quantity":1500},
        {"id":2,"date":"2022-01-05","concept":"Regalo Reyes","quantity":-150},
        {"id":3,"date":"2022-01-06","concept":"Almuerzo Reyes","quantity":-100},
    ]
    
    return render_template('index.html',pageTitle="Todos",data=registros, ingreso = select_ingreso(),gasto = select_gasto())

@app.route("/new",methods=["GET","POST"])
def create():
    form = MovementsForm()
    if request.method == "GET":
        return render_template("new.html",dataForm=form, pageTitle = 'Alta')
    else:
        

        if form.validate_on_submit():
            
            insert([ form.date.data.isoformat(),
                     form.concept.data,
                     form.quantity.data ])
            
            flash('Movimiento registrado correctamente!!!')
            return redirect(url_for('index'))
        else:
            return render_template("new.html",msgError={},dataForm=form)
    '''
    antarior sin el WTF-form
    if request.method == "GET":
        return render_template("new.html",dataForm={})
    else:
        #como recibo los datos del formulario
        errores = validateForm(request.form)
        if errores:
            return render_template("new.html",msgError=errores,dataForm=request.form)
        else:
            insert([ request.form['date'],
                     request.form['concept'],
                     request.form['quantity']  ])
            
            return redirect(url_for('index'))
        
        '''
        
@app.route ('/update/<int:id>', methods=['GET','POST'])
def update(id):
    formUpdate = MovementsForm()
    if request.method == 'GET':
        
        resultado = select_by(id)
        
        formUpdate.date.data= datetime.strptime(resultado[1], "%Y-%m-%d")
        formUpdate.concept.data = resultado[2]
        formUpdate.quantity.data = resultado[3]
        
        
        return render_template('update.html',dataForm = formUpdate, id=resultado[0],pageTitle="Editar")
    else:
        if formUpdate.validate_on_submit():
            
            update_by(id,[ formUpdate.date.data.isoformat(),
                     formUpdate.concept.data,
                     formUpdate.quantity.data ])
            
            flash('Movimiento actualizado correctamente!!!')
            return redirect(url_for('index'))
        else:

            return render_template("update.html",dataForm=formUpdate,id=id)

@app.route("/delete/<int:id>",methods=["GET","POST"])
def remove(id):
    if request.method =="GET":
    
        resultado = select_by(id)

        return render_template("delete.html",data=resultado,pageTitle="Borrar")
    else:
        
        delete_by(id)
        flash('Movimiento eliminado correctamente!!!')
        return redirect(url_for('index'))