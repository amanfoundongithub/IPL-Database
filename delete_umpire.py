import pymysql

from mysqlcursor import cur,CommitTransaction,EndConnection

def DropUmpire():
    '''
    Takes the following as input: 
    1. Jersey Number Of The Player \n
    2. The Team Of The Player \n
    '''
    try:
        name = input("Enter The Name Of The Umpire: ")

        matchID = int(input("Enter The MatchID of the Umpire: ")) 

        # Now write a query guys 
        query = "DELETE FROM Umpire where Match_No_Umpired="+str(matchID)+" AND Name='"+name+"';"

        # Now execute this query 
        cur.execute(query)
        
        CommitTransaction() 

    
    except ValueError:
        print("Invalid Data Given! Please make sure you have given correct Jersey Number!")
    
    except Exception as lol:
        print("Unexpected Error occured during SQL transaction :(\nEither some constraints are violated\nIf not,Please Try Again")