import pymysql

from mysqlcursor import cur,CommitTransaction,EndConnection

from table_print import PrintMyTable

def PitchClassfication():
    '''
    Classification as Bowler Or Batter Friendly
    '''
    try: 
        query = "SELECT SUM(Team_A_Runs)+SUM(Team_B_Runs) as Total,Stadium from Matches Group By Stadium Order By Total desc;"

        cur.execute(query) 

        x = cur.fetchall()

        for i in range(len(x)):
            if i < len(x)/2:
                print(x[i]['Stadium']+" is Batsman Friendly Pitch") 
            else:
                print(x[i]['Stadium']+" is Bowler Friendly Pitch")
        
    except Exception as lol:
        print(lol)
        print("Unexpected Error During Execution of Query") 
    pass