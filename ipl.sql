drop database if exists ipl;

create database ipl;

use ipl;

create table Team(
Team_Name varchar(255) PRIMARY KEY,
Owner varchar(255) NOT NULL,
Coach varchar(255) NOT NULL,
Points INT(10) DEFAULT 0,
Net_Run_Rate INT(10) DEFAULT 0,
Matches_Played INT(10) DEFAULT 0);

INSERT INTO Team(Team_Name,Owner,Coach) values('Gujarat Titans','CVC Capital Group','Ashish Nehra');

INSERT INTO Team(Team_Name,Owner,Coach) values('Royal Challengers Bangalore','Kingfisher Group','Sanjay Bangar');

create table Player(
    First_Name varchar(255) NOT NULL,
    Last_Name varchar(255) NOT NULL,
    Nationality varchar(255) NOT NULL,
    Team_Name varchar(255) NOT NULL,
    Jersey_No int(10) NOT NULL,
    Age int(10) NOT NULL,
    Economy int(10) DEFAULT 0,
    Total_Runs int(10) DEFAULT 0,
    Total_Wickets INT(10) DEFAULT 0,
    Total_Balls_Faced INT(10) DEFAULT 0,
    PRIMARY KEY(Jersey_No,Team_Name),
    FOREIGN KEY(Team_Name) REFERENCES Team(Team_Name)
);

create table Stadium(
    Name varchar(255) NOT NULL,
    RoadorLandmark varchar(255) NOT NULL,
    City varchar(255) NOT NULL,
    State varchar(255) NOT NULL,
    Pincode int(5) NOT NULL,
    Capacity int(20) NOT NULL,
    PRIMARY KEY(Name)
);

create table Matches(
Match_No int(10) PRIMARY KEY,
Team_A varchar(255) NOT NULL,
Team_B varchar(255) NOT NULL,
Team_A_Runs int(10) DEFAULT 0,
Team_B_Runs int(10) DEFAULT 0,
Team_A_wickets int(10) DEFAULT 0,
Team_B_wickets int(10) DEFAULT 0,
Stadium varchar(255) not NULL,
Result varchar(255),
FOREIGN KEY(Stadium) REFERENCES Stadium(Name)
);

create table Commentator(
    Match_No int(10) not NULL,
    First_Name varchar(255) not NULL,
    Last_Name varchar(255)
);

CREATE TABLE Ticket_Price(
    Name varchar(255) NOT NULL, 
    Price int(10) NOT NULL,
    PRIMARY key(Name,Price),
    FOREIGN KEY(Name) REFERENCES Stadium(Name)
);

CREATE TABLE Captain(
    Team_Name varchar(255) NOT NULL, 
    Jersey_No int(10) NOT NULL,
    Captain_Since date NOT NULL, 
    Matches_Won int DEFAULT 0,
    Matches_Lost int default 0,

    PRIMARY key(Team_Name)
    
);

CREATE TABLE Umpire(
    First_Name varchar(255) NOT NULL, 
    Last_Name varchar(255) NOT NULL, 
    Nationality varchar(255) NOT NULL, 
    Match_No_Umpired int(10) NOT NULL,
    Age int(10) NOT NULL,
    Total_Matches_Umpired int default 0,

    PRIMARY key(Match_No_Umpired,First_Name,Last_Name),
    FOREIGN KEY (Match_No_Umpired) REFERENCES Matches(Match_No)    
);

INSERT INTO Team(Team_Name,Owner,Coach) values('Chennai Super Kings','Indian Cements Ltd','Stephen Fleming');
INSERT INTO Team(Team_Name,Owner,Coach) values('Mumbai Indians','Neeta Ambani','Mahela Jayawardene');

INSERT INTO Player(First_Name,Last_Name,Nationality,Team_Name,Jersey_No,Age) values('Mahendra Singh','Dhoni','India','Chennai Super Kings',1,41);
INSERT INTO Player(First_Name,Last_Name,Nationality,Team_Name,Jersey_No,Age) values('Virat','Kohli','India','Royal Challengers Bangalore',1,34);
INSERT INTO Player(First_Name,Last_Name,Nationality,Team_Name,Jersey_No,Age) values('Hardik','Pandya','India','Gujarat Titans',1,29);
INSERT INTO Player(First_Name,Last_Name,Nationality,Team_Name,Jersey_No,Age) values('Rashid','Khan','Afghanistan','Gujarat Titans',2,24);
INSERT INTO Player(First_Name,Last_Name,Nationality,Team_Name,Jersey_No,Age) values('David','Miller','South Africa','Gujarat Titans',3,33);
INSERT INTO Player(First_Name,Last_Name,Nationality,Team_Name,Jersey_No,Age) values('Rahul','Tevatiya','India','Gujarat Titans',4,14);
INSERT INTO Player(First_Name,Last_Name,Nationality,Team_Name,Jersey_No,Age) values('Shubhman','Gill','India','Gujarat Titans',5,7);
INSERT INTO Player(First_Name,Last_Name,Nationality,Team_Name,Jersey_No,Age) values('Ruturaj','Gaikwad','India','Chennai Super Kings',2,41);
INSERT INTO Player(First_Name,Last_Name,Nationality,Team_Name,Jersey_No,Age) values('Moih','Ali','England','Chennai Super Kings',3,41);
INSERT INTO Player(First_Name,Last_Name,Nationality,Team_Name,Jersey_No,Age) values('Ravindra','Jadeja','India','Chennai Super Kings',4,41);
INSERT INTO Player(First_Name,Last_Name,Nationality,Team_Name,Jersey_No,Age) values('Deepak','Chahar','India','Chennai Super Kings',5,41);

INSERT INTO Player(First_Name,Last_Name,Nationality,Team_Name,Jersey_No,Age) values('AB','de Villiers','South Africa','Royal Challengers Bangalore',2,38);
INSERT INTO Player(First_Name,Last_Name,Nationality,Team_Name,Jersey_No,Age) values('Glen','Maxewell','Australia','Royal Challengers Bangalore',3,36);
INSERT INTO Player(First_Name,Last_Name,Nationality,Team_Name,Jersey_No,Age) values('Mohammad','Siraj','India','Royal Challengers Bangalore',4,25);
INSERT INTO Player(First_Name,Last_Name,Nationality,Team_Name,Jersey_No,Age) values('Harshal','Patel','India','Royal Challengers Bangalore',5,27);

INSERT INTO Player(First_Name,Last_Name,Nationality,Team_Name,Jersey_No,Age) values('Rohit','Sharma','India','Mumbai Indians',1,32);
INSERT INTO Player(First_Name,Last_Name,Nationality,Team_Name,Jersey_No,Age) values('Kunal','Pandya','India','Mumbai Indians',2,27);
INSERT INTO Player(First_Name,Last_Name,Nationality,Team_Name,Jersey_No,Age) values('Surayakumar','Yadav','India','Mumbai Indians',3,30);
INSERT INTO Player(First_Name,Last_Name,Nationality,Team_Name,Jersey_No,Age) values('Kieron','Pollard','West-Indies','Mumbai Indians',4,39);
INSERT INTO Player(First_Name,Last_Name,Nationality,Team_Name,Jersey_No,Age) values('Jasprith','Bumrah','India','Mumbai Indians',5,27);

INSERT INTO Stadium(Name,RoadorLandmark,City,State,PINCODE,Capacity) values('Narendra Modi Stadium','Sardar Patel Sports Enclave','Ahmedabad','Gujarat',320008,110000);
INSERT INTO Stadium(Name,RoadorLandmark,City,State,PINCODE,Capacity) values('Wankhede','Vinoo Mankad Road','Mumbai','Maharashtra',400020,33500);
INSERT INTO Stadium(Name,RoadorLandmark,City,State,PINCODE,Capacity) values('Chinnaswamy','Mahatma Gandhi Road','Bangaluru','Karnataka',560001,40000);
INSERT INTO Stadium(Name,RoadorLandmark,City,State,PINCODE,Capacity) values('Chidambaram','Wallajah Road','Chennai','Tamil Nadu',50000,45678);
INSERT INTO Ticket_Price values('Chidambaram',40000);
INSERT INTO Ticket_Price values('Chidambaram',6000);
INSERT INTO Ticket_Price values('Chidambaram',4000);

INSERT INTO Ticket_Price values('Wankhede',2000);
INSERT INTO Ticket_Price values('Wankhede',5000);
INSERT INTO Ticket_Price values('Wankhede',10000);

INSERT INTO Ticket_Price values('Chinnaswamy',30000);
INSERT INTO Ticket_Price values('Chinnaswamy',5000);
INSERT INTO Ticket_Price values('Chinnaswamy',2000);

INSERT INTO Ticket_Price values('Narendra Modi Stadium',40000);
INSERT INTO Ticket_Price values('Narendra Modi Stadium',10000);
INSERT INTO Ticket_Price values('Narendra Modi Stadium',20000);


INSERT INTO Matches(Team_A,Team_B,Match_No,Stadium) values('Gujarat Titans','Mumbai Indians',1,'Wankhede');
INSERT INTO Commentator values(1,'Ravi','Shastri');
INSERT INTO Commentator values(1,'Brett','Lee');

UPDATE Matches SET Team_A_Runs=225,Team_A_Wickets=1,Team_B_Runs=200,Team_B_Wickets=0,Result='1 won' WHERE Match_No=1;
UPDATE Player set Total_Runs=Total_Runs+100,Total_Balls_Faced=Total_Balls_Faced+50 WHERE Jersey_No=1 AND Team_Name='Gujarat Titans';
UPDATE Player set Total_Runs=Total_Runs+100,Total_Balls_Faced=Total_Balls_Faced+50 WHERE Jersey_No=2 AND Team_Name='Gujarat Titans';
UPDATE Player set Total_Runs=Total_Runs+25,Total_Balls_Faced=Total_Balls_Faced+20 WHERE Jersey_No=3 AND Team_Name='Gujarat Titans';
UPDATE Player set Total_Wickets=Total_Wickets+0,Economy=Economy+10.0 WHERE Jersey_No=3 AND Team_Name='Mumbai Indians';
UPDATE Player set Total_Wickets=Total_Wickets+1,Economy=Economy+12.5 WHERE Jersey_No=4 AND Team_Name='Mumbai Indians';
UPDATE Player set Total_Runs=Total_Runs+100,Total_Balls_Faced=Total_Balls_Faced+60 WHERE Jersey_No=1 AND Team_Name='Mumbai Indians';
UPDATE Player set Total_Runs=Total_Runs+100,Total_Balls_Faced=Total_Balls_Faced+60 WHERE Jersey_No=2 AND Team_Name='Mumbai Indians';
UPDATE Player set Total_Wickets=Total_Wickets+0,Economy=Economy+10.0 WHERE Jersey_No=3 AND Team_Name='Gujarat Titans';
UPDATE Player set Total_Wickets=Total_Wickets+0,Economy=Economy+10.0 WHERE Jersey_No=4 AND Team_Name='Gujarat Titans';

INSERT into Captain values('Gujarat Titans',1,'2022-02-02',0,0);
INSERT into Captain values('Mumbai Indians',1,'2022-02-02',0,0);
INSERT into Captain values('Royal Challengers Bangalore',1,'2022-02-02',0,0);
INSERT into Captain values('Chennai Super Kings',1,'2022-02-02',0,0);

INSERT INTO Matches(Team_A,Team_B,Match_No,Stadium) values('Chennai Super Kings','Royal Challengers Bangalore',2,'Chinnaswamy');
INSERT INTO Commentator values(2,'Harsha','Bhogle');
INSERT INTO Commentator values(2,'Ravi','Shastri');

UPDATE Matches SET Team_A_Runs=200,Team_A_Wickets=0,Team_B_Runs=190,Team_B_Wickets=1,Result='1 won' WHERE Match_No=2;
UPDATE Captain set Matches_Won=Matches_Won+1 where Team_Name='Chennai Super Kings';
UPDATE Captain set Matches_Lost=Matches_Lost+1 where Team_Name='Royal Challengers Bangalore';
UPDATE Team set Points=Points+2 where Team_Name='Chennai Super Kings';

UPDATE Player set Total_Wickets=Total_Wickets+0,Economy=Economy+12.5 WHERE Jersey_No=3 AND Team_Name='Chennai Super Kings';
UPDATE Player set Total_Wickets=Total_Wickets+1,Economy=Economy+7.5 WHERE Jersey_No=5 AND Team_Name='Chennai Super Kings';
UPDATE Player set Total_Runs=Total_Runs+30,Total_Balls_Faced=Total_Balls_Faced+30 WHERE Jersey_No=2 AND Team_Name='Royal Challengers Bangalore';
UPDATE Player set Total_Runs=Total_Runs+70,Total_Balls_Faced=Total_Balls_Faced+45 WHERE Jersey_No=3 AND Team_Name='Royal Challengers Bangalore';
UPDATE Player set Total_Runs=Total_Runs+90,Total_Balls_Faced=Total_Balls_Faced+45 WHERE Jersey_No=1 AND Team_Name='Royal Challengers Bangalore';
UPDATE Player set Total_Wickets=Total_Wickets+0,Economy=Economy+9.5 WHERE Jersey_No=4 AND Team_Name='Royal Challengers Bangalore';
UPDATE Player set Total_Wickets=Total_Wickets+0,Economy=Economy+9.5 WHERE Jersey_No=4 AND Team_Name='Royal Challengers Bangalore';
UPDATE Player set Total_Runs=Total_Runs+100,Total_Balls_Faced=Total_Balls_Faced+55 WHERE Jersey_No=3 AND Team_Name='Chennai Super Kings';
UPDATE Player set Total_Runs=Total_Runs+100,Total_Balls_Faced=Total_Balls_Faced+65 WHERE Jersey_No=1 AND Team_Name='Chennai Super Kings';

INSERT INTO Matches(Team_A,Team_B,Match_No,Stadium) values('Gujarat Titans','Chennai Super Kings',3,'Narendra Modi Stadium');
INSERT INTO Commentator values(3,'VVS','Lakshman');
INSERT INTO Commentator values(3,'Kapil','Dev');


INSERT INTO Matches(Team_A,Team_B,Match_No,Stadium) values('Royal Challengers Bangalore ','Mumbai Indians',4,'Wankhede');

INSERT INTO Umpire(First_Name,Last_Name,Match_No_Umpired,Age,Nationality) values('Marrais','maxewell',1,46,'South Africa');
INSERT INTO Umpire(First_Name,Last_Name,Match_No_Umpired,Age,Nationality) values('Paul','Reiffel',1,46,'South Africa');



-------
select first_name,jersey_no, team_name, total_wickets,total_runs from player where team_name='Gujarat Titans' or team_name='Mumbai Indians';
-------