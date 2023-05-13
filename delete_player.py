import pymysql

from mysqlcursor import cur,CommitTransaction,EndConnection

def DropPlayer():
    '''
    Takes the following as input: 
    1. Jersey Number Of The Player \n
    2. The Team Of The Player \n
    '''
    try:
        jersey = int(input("Enter The Jersey Number Of The Player: "))                   
        team =  input("Enter The Team Name The Player Plays For: ")                          
        
        # Now write a query guys 
        query = "DELETE FROM Player where Jersey_No="+str(jersey)+" AND Team_Name='"+team+"';"
        print(query)
        # Now execute this query 
        cur.execute(query)
        
        CommitTransaction() 

    
    except ValueError:
        print("Invalid Data Given! Please make sure you have given correct Jersey Number!")
    
    except Exception as lol:
        print(lol)
        print("Unexpected Error occured during SQL transaction :(\nEither some constraints are violated\nIf not,Please Try Again")