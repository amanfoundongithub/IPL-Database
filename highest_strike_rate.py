import pymysql

from mysqlcursor import cur,CommitTransaction,EndConnection

from table_print import PrintMyTable

def HighestStrikeRate():
    '''
    Shows orange cap holder
    '''
    command = "select CONCAT(First_Name,' ',Last_Name) as Name,Team_Name as `Team`,Average_Strike_Rate as `Average Strike Rate` from Player where Average_Strike_Rate in "
    command+= "(SELECT MAX(Average_Strike_Rate) from Player);"

    result = cur.execute(command) 

    lol = cur.fetchall()

    if result == 0:
        print("Empty Set: No records could be fetched")

    if len(lol) == 1:
        print("The Highest Strike Rate Belongs To "+lol[0]['Name']+" from "+lol[0]['Team']+" with his Strike Rate Being "+str(lol[0]['Average Strike Rate'])+"!")
    else:
        print("Multiple Smashers have same highest strike Rates and they are as follows: ") 
        PrintMyTable(lol,"List Of Smashers With Highest Strike Rate")
        pass 