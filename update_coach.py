import pymysql 

from mysqlcursor import cur,EndConnection,CommitTransaction 

def UpdateCoach():
    '''
    Updates coach of a given team
    '''
    try:
        tname = input("Enter The Name Of The Team: ") 
        name = input("Enter The Name Of The New Coach: ")

        if len(name) == 0:
            raise Exception 
        else:
            query = "UPDATE Team SET Coach='"+name+"' where Team_Name='"+tname+"';"
            cur.execute(query) 
            print("Coach Has Been Successfully Updated!\n")
            CommitTransaction() 
        
    except Exception as lol:
        print(lol)
        print("Please give a legitimate Coach Name!") 