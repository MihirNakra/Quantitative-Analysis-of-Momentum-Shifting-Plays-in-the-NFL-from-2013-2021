import csv
import sqlite3
from Play import Play
currentGameId = 0
usedIds = []
con = sqlite3.connect('database.db')
fileNames = ['pbp-2013.csv', 'pbp-2014.csv', 'pbp-2015.csv', 'pbp-2016.csv', 'pbp-2017.csv', 'pbp-2018.csv', 'pbp-2019.csv', 'pbp-2020.csv', 'pbp-2021.csv']

# Parse through all raw data files
for fileName in fileNames:
    with open(f'raw_data/{fileName}', newline='') as file:
        reader = csv.DictReader(file)

        # Go through each row in csv
        for row in reader:

            # If currentGameId not initialized yet
            if currentGameId == 0:
                currentGameId = row["GameId"]

            # If the next game isn't the same one as before
            if currentGameId != row['GameId']:
                currentGameId = row['GameId']
            
            # If the currentGameId is not used already, insert it into database with relevant game info
            if currentGameId not in usedIds:
                db = con.cursor()
                season = '2014'
                db.execute("INSERT INTO Game VALUES (?, ?, ?)", (currentGameId, row['GameDate'], season))
                con.commit()
                usedIds.append(currentGameId)
    
    print(f"Done with raw_data/{fileName}")
