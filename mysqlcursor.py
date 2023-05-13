import pymysql
import subprocess as sp
import pymysql.cursors


con = pymysql.connect(host='localhost',
                              user="root",
                              password="aman@2004",
                              db='ipl',
                              cursorclass=pymysql.cursors.DictCursor)


cur = con.cursor()

def CommitTransaction():
    con.commit()
    
def EndConnection():
    con.commit()
    cur.close()
    con.close()
