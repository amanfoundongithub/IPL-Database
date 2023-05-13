import pymysql

from mysqlcursor import cur,CommitTransaction,EndConnection

from table_print import PrintMyTable

def ShowPlayers():
    '''
    Shows all the players in the current IPL
    '''
    command = "SELECT CONCAT(First_Name,' ',Last_Name) AS Name,Total_Runs as `Runs Scored`,Total_Wickets as `Wickets Taken`"
    command+=" from Player;"

    result = cur.execute(command) 

    lol = cur.fetchall()

    if result == 0:
        print("Empty Set: No records could be fetched")

    else: 
        PrintMyTable(lol,"List Of All Players")
        pass  