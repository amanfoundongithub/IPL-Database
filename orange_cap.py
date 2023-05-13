import pymysql

from mysqlcursor import cur,CommitTransaction,EndConnection

from table_print import PrintMyTable

def OrangeCapHolder():
    '''
    Shows orange cap holder
    '''
    command = "select CONCAT(First_Name,' ',Last_Name) as Name,Team_Name as `Team`,Total_Runs as `Total Runs` from Player where Total_Runs in "
    command+= "(SELECT MAX(Total_Runs) from Player);"

    result = cur.execute(command) 

    lol = cur.fetchall()

    if result == 0:
        print("Empty Set: No records could be fetched")

    if len(lol) == 1:
        print("The Orange Cap Holder is "+lol[0]['Name']+" from "+lol[0]['Team']+" who has scored "+str(lol[0]['Total Runs'])+" runs")
    else:
        print("Multiple Orange Cap Holders are there and they are as follows: ") 
        PrintMyTable(lol,"List Of Orange Cap Holders")
        pass 