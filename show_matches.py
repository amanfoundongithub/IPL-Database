import pymysql

from mysqlcursor import cur,CommitTransaction,EndConnection

from table_print import PrintMyTable

def ShowMatches():
    '''
    Shows all the matches in the current IPL
    '''
    command = "SELECT Match_No as `Match Number`,Team_A as `Team 1`,Team_B as `Team 2` FROM Matches;"

    result = cur.execute(command) 

    lol = cur.fetchall()

    if result == 0:
        print("Empty Set: No records could be fetched")

    else: 
        PrintMyTable(lol,"List Of All Matches")
        pass