# Import general modules 
import pymysql
import subprocess as sp
import pymysql.cursors

# Insertion Queries 
from add_player import AddPlayer 
from add_stadium import AddStadium
from add_team import AddTeam 
from add_match import AddMatch
from add_umpire import AddUmpire

# Deletion Queries
from delete_player import DropPlayer
from delete_umpire import DropUmpire

# Update Queries
from update_coach import UpdateCoach
from age_update import UpdateAge
from age_update import UpdateUmpireAge
from after_toss import UpdateAfterToss
from after_match import UpdateAfterMatch
from add_team import UpdateCaptain 

# Selection Queries 
from show_stadium_list import ShowStadiumList 
from show_matches import ShowMatches
from add_team import FindCaptain 

# Projection Queries 
from show_players import ShowPlayers
from show_points_table import ShowPointsTable

# Search Queries 
from qualifiedteam import QualifiedTeams
from player_search import PlayerSearch

# Aggregate Queries 
from orange_cap import OrangeCapHolder 
from purple_cap import PurpleCapHolder
from highest_strike_rate import HighestStrikeRate

# Analysis Queries 
from player_of_tournament import PlayerOfTheTournament 
from pitch_classify import PitchClassfication
from best_chasing import BestChaser

def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    if(ch == 1):
        AddTeam()
        pass 
    elif(ch == 2):
        AddPlayer()
        pass 
    elif(ch == 3):
        AddStadium()
        pass
    elif(ch == 4):
        AddMatch()
        pass 
    elif(ch == 14):
        ShowStadiumList()
        pass 
    elif(ch == 18):
        ShowPointsTable()
        pass 
    elif(ch == 21):
        OrangeCapHolder()
        pass 
    elif(ch == 22):
        PurpleCapHolder() 
        pass 
    elif(ch == 23):
        HighestStrikeRate() 
        pass 
    elif(ch == 6):
        DropPlayer() 
        pass 
    elif(ch == 15):
        ShowMatches() 
    elif(ch == 16):
        ShowPlayers() 
    elif(ch == 19):
        QualifiedTeams() 
    elif(ch == 8):
        UpdateCoach() 
    elif(ch == 20):
        PlayerSearch()
    elif(ch == 9):
        UpdateAge()
    elif(ch == 11):
        UpdateAfterToss()
    elif(ch == 12):
        UpdateAfterMatch()
    elif(ch == 24):
        PlayerOfTheTournament() 
    elif(ch == 5):
        AddUmpire() 
    elif(ch == 17):
        FindCaptain() 
    elif(ch == 13):
        UpdateCaptain() 
    elif(ch == 7):
        DropUmpire() 
    elif(ch == 10):
        UpdateUmpireAge() 
    elif(ch == 26):
        PitchClassfication()
    elif(ch == 25):
        BestChaser()
    else:
        print("Error: Invalid Option")



exitvar = -1

# Main Loop 
while(True):
    #tmp = sp.call('clear', shell=True)
    
    # Can be skipped if you want to hardcode username and password
    # username = input("Username: ")
    # password = input("Password: ")

    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server 
        # port=30306,
        con = pymysql.connect(host='localhost',
                              user="root",
                              password="aman@2004",
                              db='ipl',
                              cursorclass=pymysql.cursors.DictCursor)
        #tmp = sp.call('clear', shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("Enter any key to CONTINUE>")

        with con.cursor() as cur:
            while(1):
                #tmp = sp.call('clear', shell=True)
                print("1.  Add A Team To The Database") 
                print("2.  Add A Player To The  Database")  
                print("3.  Add A Stadium To The Database")  
                print("4.  Add A Match To The Database")  # Promote Employee
                print("5.  Add An Umpire To The Database") 
                print("6.  Drop A Player From The Database")
                print("7.  Drop An Umpire From The Database")
                print("8.  Update Coach Of The Team") 
                print("9.  Update Age Of The Player On His/Her Birthday") 
                print("10. Update Age Of The Umpire On His/Her Birthday") 
                print("11. Update The Match After The Toss") 
                print("12. Update The Match After Match Has Ended") 
                print("13. Update The Captain Of The Team") 
                print("14. Show The List Of All The Stadiums") 
                print("15. Show The List Of All The Matches")
                print("16. Show The List Of All Players In The Current IPL") 
                print("17. Find The Captain Of The Current Team") 
                print("18. Show The Points Table Of The Current Season") 
                print("19. Show List Of Qualified Teams")
                print("20. Search for Player With A Given Initial Character") 
                print("21. Show The Current Orange Cap Holder in the current Season")
                print("22. Show The Current Purple Cap Holder in the current Season")
                print("23. Show The Player(s) with Highest Strike Rate Currently")
                print("24. Show The Player Of The Tournament (POTT) of the IPL season")
                print("25. Output the best chasing team of the IPL season")
                print("26. Output the classification of the stadium") 
                ch = int(input("Enter choice> "))
                #tmp = sp.call('clear', shell=True)
                if ch == exitvar:
                    con.commit() 
                    exit()
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")

    except Exception as e:
        #tmp = sp.call('clear', shell=True)
        print(e)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")