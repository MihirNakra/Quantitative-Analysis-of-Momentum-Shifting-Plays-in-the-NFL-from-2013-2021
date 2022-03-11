from Game import Game
from Play import Play
from sqlite3 import connect
import csv

SEASONS = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]

# Connect to sqlite3 database
con = connect("database.db")
db = con.cursor()

# Parse through every season
for SEASON in SEASONS:

    # Select all game ids from database
    games = db.execute("SELECT id FROM Game WHERE season=?", (SEASON,)).fetchall()

    # Parse through every gameId that was collected from database
    for gameId in games:

        # Get all plays in the current game from database
        plays = db.execute("SELECT * FROM Plays WHERE gameId=?", (gameId[0],)).fetchall()
        constructedPlays = []

        # Reconstruct plays from data in database
        for play in plays:
            constructedPlay = Play(play[9], play[1], play[2], play[3], play[7], play[8], play[4], play[5], play[6], play[10], play[11], order=play[0])
            constructedPlays.append(constructedPlay)
        
        # Initialize current game object
        game = Game(gameId, constructedPlays[1].offense, constructedPlays[1].defense, constructedPlays)
        
        teams = [game.team1, game.team2]
        counts = [game.team1count, game.team2count]

        # Intialize all statistic counters
        yards = 0
        numPasses = 0
        numComplete = 0
        numDrives = 0
        numPlays = 0

        before_ypp = 0
        before_com = 0
        before_ypd = 0

        after_ypp = 0
        after_com = 0
        after_ypd = 0

        # Goes through both teams in a current game
        for i in range(0, 1):
            currentTeam = teams[i]
            currentCount = counts[i]
            turnoverPlay = game.findTurnovers(currentTeam, currentCount)

            # If turnover play exists
            if turnoverPlay != None:

                # Collect stats for before the turnover play
                for i in range(0, turnoverPlay.order):
                    currentPlay = game.plays[i]
                    if currentPlay.offense == currentTeam:
                        try:
                            yards += currentPlay.yards
                        except:
                            pass
                        if currentPlay.result == "COM":
                            numPasses += 1
                            numComplete += 1
                        elif currentPlay.result == "INC":
                            numPasses += 1
                        
                        if currentPlay.result == "PUNT" or currentPlay.result == "FIELD GOAL" or currentPlay.isTouchdown == 1 or currentPlay.isInterception == 1 or currentPlay.isFumble == 1:
                            numDrives += 1

                        numPlays += 1
                
                # Save before turnover stats 
                before_ypp = float(yards) / numPlays
                try:
                    before_com = float(numComplete) / numPasses
                except:
                    before_com = -1
                if numDrives == 0: 
                    numDrives = 1
                before_ypd = float(yards) / numDrives

                yards = 0
                numPasses = 0
                numComplete = 0
                numDrives = 0
                numPlays = 0

                # Collect stats from after the turnover
                for i in range(turnoverPlay.order, len(plays)):
                    currentPlay = game.plays[i]
                    if currentPlay.offense == currentTeam:
                        try:
                            yards += currentPlay.yards
                        except:
                            pass
                        if currentPlay.result == "COM":
                            numPasses += 1
                            numComplete += 1
                        elif currentPlay.result == "INC":
                            numPasses += 1
                        
                        if currentPlay.result == "PUNT" or currentPlay.result == "FIELD GOAL" or currentPlay.isTouchdown == 1 or currentPlay.isInterception == 1 or currentPlay.isFumble == 1:
                            numDrives += 1

                        numPlays += 1

                # Save after turnover stats
                after_ypp = float(yards) / numPlays
                try:
                    after_com = float(numComplete) / numPasses
                except:
                    after_com = -1
                if numDrives == 0: 
                    numDrives = 1
                after_ypd = float(yards) / numDrives

                # Comment / Uncomment these depending on offensive or defensive stats
                # filename = "statistics/offensive_statistics.csv"
                filename= "statistics/defensive_statistics.csv"

                # Write statistics to a csv file
                with open(filename, 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([gameId[0], currentTeam, round(before_ypp, 3), round(after_ypp, 3), round(before_com, 3), round(after_com, 3), round(before_ypd, 3), round(after_ypd, 3)])


    print(f"Done with the {SEASON} season")
