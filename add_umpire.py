import pymysql

from mysqlcursor import cur,CommitTransaction,EndConnection

def AddUmpire():
    '''
    Takes the following as input: 
    1. Umpire Name [First_Name and Last_Name]\n
    2. Match No of the Match he is umpiring in\n
    3. Age of umpire \n
    '''
    try:
        fname,lname = input("Enter The Name Of The Umpire: ").split()
        
        matchID = int(input("Enter The Match Number Of The Match He is Umpiring In: ")) 

        nationality = input("Enter The Nationality Of The Umpire: ") 

        age = int(input("Enter The Age Of The Umpire: "))

        # Now write a query guys 
        query = "INSERT INTO Umpire(First_Name,Last_Name,Match_No_Umpired,Age,Nationality)"
        query +=" values('"+fname+"','"+lname+"',"+str(matchID)+","+str(age)+",'"+nationality+"');"
        
        # Now execute this query 
        print(query)
        cur.execute(query) 
        CommitTransaction() 
    
    except ValueError:
        print("Unexpected Error Due To Violation Of Values")
    except Exception as lol:
        print("Unexpected Error occured during SQL transaction :(\nEither some constraints are violated\nIf not,Please Try Again")
    