import sqlite3
from config import *


class Conexion:
    pass
'''''
    def __init__(self,querySql):
        self.con = sqlite3.connect(ORIGIN_DATA)
        self.cur = con.cursor()
        self.res = cur.execute(querySql)
'''        