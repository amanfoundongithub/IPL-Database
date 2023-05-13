import pymysql

from mysqlcursor import cur,CommitTransaction,EndConnection

def AddStadium():
    '''
    Takes the following as input: 
    1. Name Of Stadium\n
    2. Landmark Of The Stadium\n
    3. City\n
    4. State and PINCODE\n
    5. Capacity\n
    '''
    try:
        fname =  input("Enter The Name Of The Stadium: ")             # Stadium Name 
        lname =  input("Enter The Landmark Of The Stadium: ")         # Landmark  
        nation = input("Enter The City Of The Stadium: ")             # City 
        tname =  input("Enter The State Of The Stadium: ")            # State 
        jersey = int(input("Enter The PINCODE Of The Stadium: "))     # PINCODE 
        age    = int(input("Enter The Capacity Of The Stadium: "))    # Capacity
        
        # Now write a query guys 
        query = "INSERT INTO Stadium(Name,RoadorLandmark,City,State,PINCODE,Capacity)"
        query +=" values('"+fname+"','"+lname+"','"+nation+"','"+tname+"',"+str(jersey)+","+str(age)+");"
        
        print(query)
        
        # Now execute this query 
        cur.execute(query) 

        # Now find ticket prices 
        prices = list(set(map(int,input("Enter The Ticket Prices, Seperated By Spaces: ").split()))) 

        for i in prices: 
            query = "INSERT INTO Ticket_Price" 
            query+= " values('"+fname+"',"+str(i)+");"
            print(query)
            cur.execute(query)

        CommitTransaction() 
    

    except ValueError:
        print("Invalid Data Given! Please Make Sure You Have Entered Correct Capacity or PINCODE")
    
    except Exception as lol:
        print("Unexpected Error occured during SQL transaction :(\nEither some constraints are violated\nIf not,Please Try Again")
    