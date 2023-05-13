import pymysql

from mysqlcursor import cur,CommitTransaction,EndConnection

def AddMatch():
    '''
    Takes the following as input: 
    Match No\n
    1. Team 1\n
    2. Team 2\n
    3. Commentators\n
    '''
    try:
        jersey = int(input("Enter The Match_No: "))                   # Match number  
        lname =  input("Enter The Name Of Team 1: ")                        # Team 1   
        nation = input("Enter The Name Of Team 2: ")                        # team 2
        stadium=input("Enter The Name of Stadium: ")
        # Now write a query guys 
        query = "INSERT INTO Matches(Team_A,Team_B,Match_No,Stadium)"
        query +=" values('"+lname+"','"+nation+"',"+str(jersey)+",'"+stadium+"');"

        # Now execute this query 
        print(query)
        cur.execute(query) 

        n = int(input("Enter Number of Commentator(s): "))

        for i in range(n):
            fname,lname = input("Enter The First and Last Name Of Commentator, seperated by space: ").split()
            query = "INSERT INTO Commentator" 
            query+= " values("+str(jersey)+",'"+fname+"','"+lname+"');"
            print(query)
            cur.execute(query) 
        
        CommitTransaction() 

    
    except ValueError:
        print("Invalid Data Given! Please Make Sure You Have Entered Match Number")
    
    except Exception as lol:
        print("Unexpected Error occured during SQL transaction :(\nEither some constraints are violated\nIf not,Please Try Again")
    