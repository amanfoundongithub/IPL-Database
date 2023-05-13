import pymysql

from mysqlcursor import cur,CommitTransaction,EndConnection

from table_print import PrintMyTable

def ShowStadiumList():
    '''
    Shows all the stadiums in the current season 
    '''
    command = "SELECT Name as `Name Of Stadium`,PINCODE FROM Stadium;"

    result = cur.execute(command) 

    if result == 0:
        print("Empty Set: No records could be fetched")
    else:
        PrintMyTable(cur.fetchall(),"List Of Stadiums")