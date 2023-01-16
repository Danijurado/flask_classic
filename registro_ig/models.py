import sqlite3
from config import *
from registro_ig.conexion import Conexion

def select_ingreso():
    connectSelect_ingreso = Conexion("SELECT sum(quantity) FROM movement WHERE quantity>0")
    resultado = connectSelect_ingreso.res.fetchall()
    connectSelect_ingreso.con.close()
    return resultado[0][0]

def select_gasto():
    connectSelect_gasto = Conexion("SELECT sum(quantity) FROM movement WHERE quantity<0")
    resultado = connectSelect_gasto.res.fetchall()
    connectSelect_gasto.con.close()
    return resultado[0][0]
    

def select_all():
    connect = Conexion("select id,date,concept,quantity from movement order by date;")
    filas = connect.res.fetchall()#capturo las filas de datos
    columnas= connect.res.description#capturo los nombres de columnas

    #objetivo crear una lista de diccionario con filas y columnas

    resultado =[]#lista para guadar diccionario
   
    for fila in filas:
        dato={}#diccionario para cada registro
        posicion=0#posicion de columna

        for campo in columnas:
            dato[campo[0]]=fila[posicion]
            posicion += 1
        resultado.append(dato)

    connect.con.close()

    return resultado


def insert(registro):
    connectInsert = Conexion("insert into movement(date,concept,quantity) values(?,?,?)",registro)
    connectInsert.con.commit()#funcion que registra finalmente
    connectInsert.con.close()
   

def select_by(id):
    connectSelectBy=Conexion(f"select id,date,concept,quantity from movement where id={id}")
    resultado = connectSelectBy.res.fetchall()
    connectSelectBy.con.close()
    return resultado[0]

def delete_by(id):
    connectDeleteBy=Conexion(f"delete from movement where id={id}")
    connectDeleteBy.con.commit()
    connectDeleteBy.con.close()
 
def update_by(id,registro):
    connectUpdate = Conexion('UPDATE movement set date=?,concept=?,quantity=? WHERE id={id}',registro)
    connectUpdate.con.commit()
    connectUpdate.con.close()
    
            