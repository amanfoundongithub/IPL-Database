import pymysql 

from mysqlcursor import cur,EndConnection,CommitTransaction 

def UpdateAge():
    '''
    Updates age of a player 
    '''
    try:
        tname = input("Enter The Jersey Number Of The Player: ") 
        name = input("Enter The Team Of The Player: ")

        if len(name) == 0 or len(tname) == 0:
            raise Exception 
        else:
            query = "UPDATE Player SET Age=Age+1 where Team_Name='"+name+"' and Jersey_No='"+tname+"';"
            cur.execute(query) 
            #print("Coach Has Been Successfully Updated!\n")
            CommitTransaction() 
        
    except Exception as lol:
        print("Please give a legitimate answer!") 

def UpdateUmpireAge():
    '''
    Updates age of a umpire 
    '''
    try:
        tname = input("Enter The Name Of The Umpire: ")
        name = int(input("Enter The Team Of The Player: "))

        if len(tname) == 0:
            raise Exception 
        else:
            query = "UPDATE Umpire SET Age=Age+1 where Name='"+tname+"' and Match_No_Umpired="+str(name)+";"
            print(query) 
            cur.execute(query) 
            
            CommitTransaction() 
        
    except Exception as lol:
        print(lol)
        print("Please give a legitimate answer!")
    
