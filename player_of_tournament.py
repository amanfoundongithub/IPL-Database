import pymysql 

from mysqlcursor import cur,EndConnection,CommitTransaction 

def PlayerOfTheTournament() -> None:
    try:
        # Now declare player of the tournament 
        query = "SELECT CONCAT(First_Name,' ',Last_Name) as Name,Jersey_No as Jersey,Team_Name as Team,Average_Strike_Rate as ARR,Total_Runs as Runs,Total_Wickets as Wickets from Player ORDER BY Total_Runs DESC LIMIT 3;"

        cur.execute(query) 

        rows = cur.fetchall() 

        rows = list(rows)

        rows.sort(key=lambda x:x['ARR'],reverse=True)

        batcandidate = rows[0] 

        query = "SELECT CONCAT(First_Name,' ',Last_Name) as Name,Jersey_No as Jersey,Team_Name as Team,Economy as ARR,Total_Wickets as Wickets,Total_Runs as Runs from Player ORDER BY Total_Wickets DESC LIMIT 3;"

        cur.execute(query) 

        rows = cur.fetchall()

        rows = list(rows)

        rows.sort(key=lambda x:x['ARR'],reverse=True)

        bowlcandidate = rows[0] 

        batcalculate = batcandidate['Runs'] + 40*batcandidate['Wickets']

        bowlcalculate = bowlcandidate['Runs'] + 40*bowlcandidate['Wickets']

        if(batcalculate > bowlcalculate):
            potname = batcandidate['Name'] 
            potjersey = batcandidate['Jersey'] 
            potteam = batcandidate['Team']
            potruns = batcandidate['Runs'] 

            print("The Player Of The Tournament Is "+potname+" (Jersey No: "+str(potjersey)+") from "+potteam+" with "+str(potruns)+" runs")
        
        else:
            potname = bowlcandidate['Name'] 
            potjersey = bowlcandidate['Jersey'] 
            potteam = bowlcandidate['Team']
            potruns = bowlcandidate['Runs'] 

            print("The Player Of The Tournament Is "+potname+" (Jersey No: "+str(potjersey)+") from "+potteam+" with "+str(potruns)+" wickets")

        pass 
    except Exception as lol:
        print(lol) 
