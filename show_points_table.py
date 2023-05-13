import pymysql
from mysqlcursor import cur,CommitTransaction,EndConnection
from table_print import PrintMyTable

def ShowPointsTable():
    '''
    Shows points table of the current season
    '''
    command = "SELECT Team_Name AS`Name Of The Team`,Matches_Played as `Matches Played`,Points,Net_Run_Rate as NRR FROM Team ORDER BY Points DESC,NRR DESC;"

    result = cur.execute(command) 

    if result == 0:
        print("Empty Set: No records could be fetched")
    else:
        PrintMyTable(cur.fetchall(),"Points Table Of The Current IPL")