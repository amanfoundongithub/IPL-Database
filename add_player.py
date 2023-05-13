import pymysql

from mysqlcursor import cur,CommitTransaction,EndConnection


def AddPlayer():
    '''
    Takes the following as input: 
    1. Name Of The Player [F,L]\n
    2. Jersey No Of The Player \n
    3. Nationality of Player\n
    4. Team Of the Player\n
    5. Age of the Player\n
    '''
    try:
        fname =  input("Enter The First Name  Of The Player: ")
        lname =  input("Enter The Last  Name  Of The Player: ") 
        nation = input("Enter The Nationality Of The Player: ") 
        tname =  input("Enter The Team Name   Of The Player: ")
        jersey = int(input("Enter The Jersey No.  Of The Player: "))
        age    = int(input("Enter The Age of the Player: "))
        
        # Now write a query guys 
        query = "INSERT INTO Player(First_Name,Last_Name,Nationality,Team_Name,Jersey_No,Age)"
        query +=" values('"+fname+"','"+lname+"','"+nation+"','"+tname+"',"+str(jersey)+","+str(age)+");"
        
        # Now execute this query 
        print(query);
        cur.execute(query) 
        CommitTransaction() 

    
    except ValueError:
        print("Invalid Data Given! Please Make Sure You Have Entered Correct Age or Jersey Number")
    
    except Exception as lol:
        print(lol) 
        print("Unexpected Error occured during SQL transaction :(\nEither some constraints are violated\nIf not,Please Try Again")
    

    