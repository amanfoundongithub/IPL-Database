import pymysql 

from mysqlcursor import cur,EndConnection,CommitTransaction 

def UpdateAfterMatch():
    # Get The Entry 
    try:
        
        # Enter The MatchID to uniquely identify the match 
        matchID = int(input("Enter The Match Number Of The Match: "))         
        
        cur.execute("Select Team_A as Defender,Team_B as Chaser from Matches where Match_No="+str(matchID)+";")

        x = cur.fetchall()

    
        # x = 'O'
        if(len(x) == 0):
            raise Exception 
        else:
            #defender="Mumbai Indians" 
            #chaser="Pakistan"
            
            defender = x[0]['Defender'] 
            chaser   = x[0]['Chaser'] 
            query = "Update Team set matches_played=matches_played+1 where team_name='"
            query+= defender+"' or team_name='"+chaser+"';"
            print(query)
            cur.execute(query)
            print("Enter The Score Of "+str(defender)+" in the match [in the format:Runs-Wickets] :- ",end="")
            score1 = input()

            print("Enter The Score Of "+str(chaser)+" in the match [in the format:Runs-Wickets] :- ",end="") 
            score2 = input()

            
            
            runs1,wickets1 = map(int,score1.split('-'))

            runs2,wickets2 = map(int,score2.split('-'))

            print("Did The Match Ended Peacefully ? [Answer as Yes/No] ",end="")
            res = input()

            if(res == 'Yes'):
                if score1 > score2:
                    result = '1 won'
                    winningteam=defender
                    losingteam=chaser
                elif score2 > score1:
                    winningteam=chaser
                    losingteam=defender
                    result = '2 won'
                else:
                    result = 'Tie' 
            else:
                result = 'No Result'

            query = "UPDATE Matches SET Team_A_Runs="+str(runs1)+",Team_A_Wickets="+str(wickets1) 
            query+= ",Team_B_Runs="+str(runs2)+",Team_B_Wickets="+str(wickets2)
            query+= ",Result='"+result+"' WHERE Match_No="+str(matchID)+";"
            
            print(query)
            cur.execute(query)

            CommitTransaction()
            
            query = "UPDATE Captain set Matches_Won=Matches_Won+1 where Team_Name='"+str(winningteam)+"';"
            
            print(query)
            cur.execute(query)
            CommitTransaction()
            query = "UPDATE Captain set Matches_Lost=Matches_Lost+1 where Team_Name='"+str(losingteam)+"';"
             
            print(query)
            cur.execute(query)
            CommitTransaction()
               
            if(result=='Tie'):
                query = "UPDATE Team set Points=Points+1 where Team_Name='"+losingteam+"' or Team_Name='"+winningteam+"';"
            else:
                query = "UPDATE Team set Points=Points+2 where Team_Name='"+winningteam+"';"
            
            print(query)
            cur.execute(query)
            CommitTransaction()    
             
            
            # Batting for Team 1 [Defender]
            print("Enter The Number Of Players Who Did Batting For "+str(defender)+": ",end="")
            batted = int(input())

            for i in range(batted):
                print()
                print("Player #",i + 1) 
                print("Enter The Jersey Number Of The Player: ",end="") 
                jersey = int(input())

                print("Enter The Number Of Runs Scored By The Player: ",end="")
                runs = int(input())

                print("Enter The Number Of Balls Faced By The Player: ",end="")
                balls = int(input())

                query = "UPDATE Player set Total_Runs=Total_Runs+"+str(runs)+",Total_Balls_Faced=Total_Balls_Faced+"+str(balls)
                query+= " WHERE Jersey_No="+str(jersey)+" AND Team_Name='"+defender+"';"
                print(query)
                cur.execute(query)
                CommitTransaction()

                query = "UPDATE Player set Average_Strike_Rate=(Total_Runs/Total_Balls_Faced)*100"
                query+= " WHERE Jersey_No="+str(jersey)+" AND Team_Name='"+defender+"';"

                cur.execute(query)
                CommitTransaction()
            
            # Bowling for Team 2 [Chaser]
            print("Enter The Number Of Players Who Did Bowling For "+str(chaser)+": ",end="")
            batted = int(input())

            for i in range(batted):
                print()
                print("Player #",i + 1) 
                print("Enter The Jersey Number Of The Player: ",end="") 
                jersey = int(input())

                print("Enter The Number Of Overs Bowled By The Bowler: ",end="") 
                overs = float(input())

                print("Enter The Number Of Runs Conceeded By The Bowler: ",end="")
                runs = int(input())

                print("Enter The Number Of Wickets Taken By The Bowler: ",end="")
                wickets = int(input())

                # Now calculate number of balls
                balls = int(overs)*6 + int(overs*10 - 10*int(overs)) 

                economy = (runs/balls)*6 

                query = "UPDATE Player set Total_Wickets=Total_Wickets+"+str(wickets)+",Economy=Economy+"+str(economy)
                query+= " WHERE Jersey_No="+str(jersey)+" AND Team_Name='"+chaser+"';"
                print(query)

                cur.execute(query)
                CommitTransaction()
            
            # Batting of Chaser [Team 2]
            print("Enter The Number Of Players Who Did Batting For "+str(chaser)+": ",end="")
            batted = int(input())

            for i in range(batted):
                print()
                print("Player #",i + 1) 
                print("Enter The Jersey Number Of The Player: ",end="") 
                jersey = int(input())

                print("Enter The Number Of Runs Scored By The Player: ",end="")
                runs = int(input())

                print("Enter The Number Of Balls Faced By The Player: ",end="")
                balls = int(input())

                query = "UPDATE Player set Total_Runs=Total_Runs+"+str(runs)+",Total_Balls_Faced=Total_Balls_Faced+"+str(balls)
                query+= " WHERE Jersey_No="+str(jersey)+" AND Team_Name='"+chaser+"';"
                print(query)
                cur.execute(query)
                CommitTransaction()

                query = "UPDATE Player set Average_Strike_Rate=(Total_Runs/Total_Balls_Faced)*100"
                query+= " WHERE Jersey_No="+str(jersey)+" AND Team_Name='"+chaser+"';"
                cur.execute(query)
                CommitTransaction()
            
            # Bowling Of Defender [Team 1]
            print("Enter The Number Of Players Who Did Bowling For "+str(defender)+": ",end="")
            batted = int(input())

            for i in range(batted):
                print()
                print("Player #",i + 1) 
                print("Enter The Jersey Number Of The Player: ",end="") 
                jersey = int(input())

                print("Enter The Number Of Overs Bowled By The Bowler: ",end="") 
                overs = float(input())

                print("Enter The Number Of Runs Conceeded By The Bowler: ",end="")
                runs = int(input())

                print("Enter The Number Of Wickets Taken By The Bowler: ",end="")
                wickets = int(input())

                # Now calculate number of balls
                balls = int(overs)*6 + int(overs*10 - 10*int(overs)) 

                economy = (runs/balls)*6

                query = "UPDATE Player set Total_Wickets=Total_Wickets+"+str(wickets)+",Economy=Economy+"+str(economy)
                query+= " WHERE Jersey_No="+str(jersey)+" AND Team_Name='"+defender+"';"
                
                print(query)
                cur.execute(query)
                CommitTransaction()

            CommitTransaction()
             
    except Exception as lol:
        print(lol) 
        print("Unexpected Error During SQL Query Transaction or While Taking Input") 
        pass 