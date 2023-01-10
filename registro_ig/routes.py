from registro_ig import app
from flask import render_template


@app.route('/')
def index():
    datos_mov=[
        {"id":1,"date":"2022-01-01","concept":"Sueldo","quantity":1500},
        {"id":2,"date":"2022-01-05","concept":"Regalo Reyes","quantity":-150},
        {"id":3,"date":"2022-01-06","concept":"Almuerzo Reyes","quantity":-100},
    ]
    
    return render_template('index.html',pageTitle="Todos",data=datos_mov)