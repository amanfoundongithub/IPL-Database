import pymysql

from mysqlcursor import cur,CommitTransaction,EndConnection

def AddTeam():
    '''
    Takes the following as input: 
    1. Team Name\n
    2. Owner\n
    3. Coach\n
    '''
    try:
        fname =  input("Enter The Name Of The Team: ")              # Stadium Name 
        lname =  input("Enter The owner Of The Team: ")             # Landmark  
        nation = input("Enter The Coach Of The Team: ")             # City 

        # capname = int(input("Enter The Jersey Number Of The Captain Of The Team: ")) # Name
        # capsince = input("Enter The Date [YYYY-MM-DD] since the Captain has been appointed: ") 

        
        # Now write a query guys 
        query = "INSERT INTO Team(Team_Name,Owner,Coach)"
        query +=" values('"+fname+"','"+lname+"','"+nation+"');"
        
        # Now execute this query 
        cur.execute(query) 
        print(query)

        # query = "INSERT INTO Captain(Jersey_No,Team_Name,Captain_Since)"
        # query+= " values("+str(capname)+",'"+fname+"','"+capsince+"');"

        # cur.execute(query)

        CommitTransaction() 

    except Exception as lol:
        print(lol) 
        print("Unexpected Error occured during SQL transaction :(\nEither some constraints are violated\nIf not,Please Try Again")

def FindCaptain():
    '''
    returns captain of the team
    '''
    try:
        tname = input("Enter The Name Of The Team: ") 

        query = "SELECT CONCAT(First_Name,' ',Last_Name) as Name from Player where Jersey_No IN"
        query+= "(SELECT Jersey_No from Captain where Team_Name='"+tname+"') AND Team_Name='"+tname+"';"

        cur.execute(query)

        x = cur.fetchall()

        print("The captain of "+tname+" is "+x[0]['Name'])     
    except Exception as lol:
        print("Error") 


def UpdateCaptain():
    '''
    returns captain of the team
    '''
    try:
        tname = input("Enter The Name Of The Team: ") 
        capname = int(input("Enter Jersey No Of The New Captain: "))
        capyear = input("Enter The Date[YYYY-MM-DD] since the Player has been captain: ") 

        query = "UPDATE Captain set Jersey_No="+str(capname)+",Matches_Won=0,Matches_Lost=0,Captain_Since='"+capyear
        query+= "' where Team_Name='"+tname+"';"
        print(query)
        cur.execute(query)
        CommitTransaction()     
    except Exception as lol:
        print("Error") 