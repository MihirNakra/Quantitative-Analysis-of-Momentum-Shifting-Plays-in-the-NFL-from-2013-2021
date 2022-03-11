import csv
import sqlite3
from Play import Play
currentGameId = 0
playList = []
fileNames = ['pbp-2013.csv', 'pbp-2014.csv', 'pbp-2015.csv', 'pbp-2016.csv', 'pbp-2017.csv', 'pbp-2018.csv', 'pbp-2019.csv', 'pbp-2020.csv', 'pbp-2021.csv']
games = {}

# Parse through all raw data files
for name in fileNames:

    # Open current file
    with open(name, newline='') as file:
        reader = csv.DictReader(file)

        # Parse through every row in csv file
        for row in reader:

            # If currentGameId not initialized yet
            if currentGameId == 0:
                currentGameId = row["GameId"]

            # If the next game isn't the same one as before
            if currentGameId != row['GameId']:

                # If there is already a dictionary entry for the currentGameId
                if currentGameId in games:
                    games.update({currentGameId: games[currentGameId] + playList})
                else:
                    games.update({currentGameId: playList})
                playList = []

                # Reinitialize currentGameId
                currentGameId = row['GameId']

            result = row['PlayType']
            if result == "PASS":
                if row['IsIncomplete'] == "1": 
                    result = "INC"
                else:
                    result = "COM"

            # Construct a play object and add it to list of play objects
            currentPlay = Play(row['GameId'], row['Quarter'], row['Minute'], row['Second'], row['OffenseTeam'], row['DefenseTeam'], row['Yards'], result, row['IsTouchdown'], row['IsInterception'], row['IsFumble'])
            playList.append(currentPlay)        
        
        print(f"Done initializing {name}")

# Parse through all plays and order them chronologically in their respective games
for game in games:
    orderedPlays = Play.organizePlays(games[game])
    games.update({game: orderedPlays})
    print(f"Done ordering game: {game}")

# Parse through all games and save them into the database
for gameId in games:
    playOrder = 0
    for play in games[gameId]:
            con = sqlite3.connect("database.db")
            db = con.cursor()
            db.execute("INSERT INTO Plays VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (playOrder, play.quarter, play.minute, play.second, play.yards, play.result, play.isTouchdown, play.offense, play.defense, play.gameId, play.isInterception, play.isFumble))
            con.commit()
            playOrder += 1
    
    print(f"Done saving game: {gameId}")



