<h1>Project Implementation</h1>
<h3>Team No: 49

Database MiniWorld: IPL</h3>
# Interface Implementation 
The Python file that actually implements the interface is `terminal.py`. 
To run the terminal, go to the same directory and run the following command:
```
>>> python3 terminal.py
```
The interface will be loaded on the screen. Then, you have to press any Key to continue to the main menu.

After going to the main menu, you will be shown the list of commands along with the numbers of the commands. Enter the command number in the command prompt.

The following commands are implemented: 

1.  Add A Team To The Database
- Takes the team name,owner,coach as input and adds the team to database.
2.  Add A Player To The  Database
- Takes the Player name, jersey number, nationality, team and age of the player as input and adds him to the database.
3.  Add A Stadium To The Database
- Takes stadium name,address and pincode of the stadium as input and adds it to the database.
4.  Add A Match To The Database
- Takes the match number, team name(s) and the commentator(s) as input and adds the match to the database.
5.  Add An Umpire To The Database
- takes the name of the umpire, match no he is umpiring, nationality and the age of the Umpire and Add it to the database.
6.  Drop A Player From The Database
- takes the jersey number and the team name of the player as input and deletes the player from the database.
7.  Drop An Umpire From The Database
- takes the match number umpired by the umpire and the name of the umpire and deletes the umpire from the database. 
8.  Update Coach Of The Team
- takes the team name and the coach name as input and updates the coach name of the team to the desired name.
9.  Update Age Of The Player On His/Her Birthday
- takes the player's jersey number and team name and updates player's age. 
10. Update Age Of The Umpire On His/Her Birthday
- takes the umpire's name and match number and updates umpire's age. 
11. Update The Match After The Toss
- updates match after toss has happened
12. Update The Match After Match Has Ended
- updates match after it has ended 
13. Update The Captain Of The Team
- updates the captain of the team if it changes.
14. Show The List Of All The Stadiums
- displays list of all stadiums
15. Show The List Of All The Matches
- displays list of all matches in current IPL season
16. Show The List Of All Players In The Current IPL
- Displays list of all players in the current IPL season
17. Find The Captain Of The Current Team
- Finds the captain of the team
18. Show The Points Table Of The Current Season
- Displays points table of the current season
19. Show List Of Qualified Teams
- Displays names of the teams that have qualified for the playoffs.
20. Search for Player With A Given Initial Character
- Search for player names which have the given initial character.
21. Show The Current Orange Cap Holder in the current Season
- Displays the name of the orange cap holder(s)
22. Show The Current Purple Cap Holder in the current Season
- Displays the name of the purple cap holder(s)
23. Show The Player(s) with Highest Strike Rate Currently
- Displays the name(s) of the player(s) with highest strike rate.
24. Show The Player Of The Tournament (POTT) of the IPL season
- Finds the Player Of The Tournament of the current IPL season.
25. Output the best chasing team of the IPL season
- Finds the best chasing team of the IPL season.
26. Output the classification of the stadium
- Output the pitches as batsman and bowler friendly. 