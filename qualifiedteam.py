import pymysql
from mysqlcursor import cur,CommitTransaction,EndConnection

def QualifiedTeams():
    '''
    Takes Nothing as input , return teams with points >= 16 
    '''
    try:
        # Now write a query guys 
        query = "SELECT Team_Name AS Name from Team where Points>=6;"

        # Now execute this query 
        cur.execute(query)

        lol = cur.fetchall() 

        if(len(lol) == 0):
            print("No Team, As Of Now, Have Qualified For The PlayOffs!")
        elif(len(lol) == 1):
            print("Only "+lol[0]['Name']+" has qualified for the Qualifiers!")
        else:
            print("The following teams have qualified for the Qualifier: ")
            for i in lol:
                print(i['Name']) 

    
    except Exception as lol:
        print("Unexpected Error occured during SQL transaction :(\nEither some constraints are violated\nIf not,Please Try Again")