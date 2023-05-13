import pymysql

from mysqlcursor import cur,CommitTransaction,EndConnection

from table_print import PrintMyTable

def PurpleCapHolder():
    '''
    Shows orange cap holder
    '''
    command = "select CONCAT(First_Name,' ',Last_Name) as Name,Team_Name as `Team`,Total_Wickets as `Total Wickets` from Player where Total_Wickets in "
    command+= "(SELECT MAX(Total_Wickets) from Player);"

    result = cur.execute(command) 

    lol = cur.fetchall()

    if result == 0:
        print("Empty Set: No records could be fetched")

    if len(lol) == 1:
        print("The Purple Cap Holder is "+lol[0]['Name']+" from "+lol[0]['Team']+" who has taken "+str(lol[0]['Total Wickets'])+" wickets")
    else:
        print("Multiple Purple Cap Holders are there and they are as follows: ") 
        PrintMyTable(lol,"List Of Purple Cap Holders")
        pass 