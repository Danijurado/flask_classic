import sqlite3
from config import *
#from conexion import conexion
'''''
def conection(querySql):
    con = sqlite3.connect(ORIGIN_DATA)
    cur = con.cursor()
    res = cur.execute(querySql)
'''    

def select_all():
    con = sqlite3.connect(ORIGIN_DATA)
    cur = con.cursor()
    
    res = cur.execute('SELECT id,date,concept,quantity from movement order by date')
    
    filas = res.fetchall() #capturo las filas de datos
    columnas = res.description #capturo los nombres de columnas
    
    resultado = []
    
    for fila in filas:
        dato = {}
        posicion = 0
        
        for campo in columnas:
            dato[campo[0]] = fila[posicion]
            posicion += 1
        resultado.append(dato)
    con.close()    
    return resultado

def insert(registro):
    con = sqlite3.connect(ORIGIN_DATA)
    cur = con.cursor()
    
    cur.execute('insert into movement(date, concept, quantity) values(?,?,?)',registro)
    con.commit()
    con.close()
    
def select_by(id):
    con = sqlite3.connect(ORIGIN_DATA)
    cur = con.cursor()
    
    res = cur.execute(f'SELECT id,date,concept,quantity from movement where id={id}')
    
    resultado = res.fetchall()
    con.close()
    return resultado[0] 

def delete(id):
    con = sqlite3.connect(ORIGIN_DATA)
    cur = con.cursor()
    cur.execute(f'delete from movement where id={id}')
    con.commit()
    con.close()
    
    
 
            