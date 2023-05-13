import pymysql

from mysqlcursor import cur,CommitTransaction,EndConnection

def BestChaser():
    '''
    Find Best Chasing IPL team
    '''
    try:
        query = "SELECT Team_B as Team,COUNT(*) as Wins from Matches where Result='2 won' Group By Team_B order by Wins desc limit 1;" 
        cur.execute(query)
        x = cur.fetchall()
        top_team = x[0]['Team'] 
        print("The Best Chasing Team is "+top_team+" with "+str(x[0]['Wins'])+" wins.")
    
    except Exception as lol:
        print(lol)
        print("Unexpected Error While Processing Query")