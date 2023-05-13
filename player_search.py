import pymysql
from mysqlcursor import cur,CommitTransaction,EndConnection

def PlayerSearch():
    '''
    Takes Nothing as input , return Player Name starting with m
    '''
    try:
        m = input("Enter The Starting Alphabet: ") 
        # Now write a query guys 
        query = "SELECT CONCAT(First_Name,' ',Last_Name) as Name from Player where First_Name like '"+m+"%';"

        # Now execute this query 
        cur.execute(query)

        lol = cur.fetchall() 

        if(len(lol) == 0):
            print("No Players Found With Given Starting Alphabet")
        elif(len(lol) == 1):
            print("Only one Player Found: "+lol[0]['Name']) 
        else:
            print("Following Players Are Found: ")
            for i in lol:
                print(i['Name']) 

    
    except Exception as lol:
        print("Unexpected Error occured during SQL transaction :(\nEither some constraints are violated\nIf not,Please Try Again")