from registro_ig import app
from flask import render_template, request, redirect, url_for
from registro_ig.models import select_all,insert,select_by,delete
from datetime import date

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
    
    return render_template('index.html',pageTitle="Todos",data=registros)

@app.route("/new",methods=["GET","POST"])
def create():

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
                    request.form['quantity']])
            
            return redirect(url_for('index'))
        
@app.route('/delete/<int:id>',methods=["GET","POST"])
def remove(id):
    if request.method =='GET':
        resultado = select_by(id)
        return render_template('delete.html',data = resultado)
    else:
        delete(id)
        return redirect(url_for('index'))
    