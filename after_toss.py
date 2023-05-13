import pymysql 

from mysqlcursor import cur,EndConnection,CommitTransaction 

def UpdateAfterToss():
    # Get The Entry 
    try:
        # Enter The MatchID to uniquely identify the match 
        matchID = int(input("Enter The Match Number Of The Match: ")) 

        cur.execute("SELECT TEAM_A,TEAM_B FROM Matches WHERE Match_No="+str(matchID)+";") 

        x = cur.fetchall()
        print(x)
        if(len(x) == 0):
            raise Exception
        else:
            main = x[0] 

            # Ask The Toss Winning Team Now
            winner = input("Enter The Toss Winning Team: ")

            if((winner != x[0]['TEAM_A'] and winner != x[0]['TEAM_B']) or (winner == x[0]['TEAM_A'] and winner == x[0]['TEAM_B'])):
                raise Exception 
            
            loser = None 
            if(x[0]['TEAM_A'] == winner):
                loser = x[0]['TEAM_B']
            elif(x[0]['TEAM_B'] == winner):
                loser = x[0]['TEAM_A']
            
            res = input("What did the Toss winning team asked for? [Answer as Bat/Field] ") 

            if(res == 'Bat'):
                team_A = winner 
                team_B = loser 
            else:
                team_A = loser 
                team_B = winner 
            
            query = "UPDATE Matches Set Team_A='"+team_A+"',Team_B='"+team_B+"' where Match_No="+str(matchID)+";"

            cur.execute(query)
            CommitTransaction()
            
    except Exception as lol:
        pass 