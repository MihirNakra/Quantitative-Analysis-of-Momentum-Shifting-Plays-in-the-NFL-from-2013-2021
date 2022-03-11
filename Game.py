
# Helper class to store all relevant game information
class Game:

    def __init__(self, gameId, team1, team2, plays):
        self.gameId = gameId
        self.team1 = team1
        self.team2 = team2
        self.plays = plays
        self.team1count = 0
        self.team2count = 0
        for play in plays:
            if play.offense == self.team1:
                self.team1count += 1
            else:
                self.team2count += 1
        self.NUM_DISCARDED_PLAYS = 6
    

    # Function that goes through all plays and returns a turnover play that fits criteria
    def findTurnovers(self, team, totalCount):
        playCount = 0
        for play in self.plays:
            if play.offense == team:
                playCount += 1
                
            if play.defense == team and play.isInterception == 1 or play.isFumble == 1:
                if playCount > 6 and playCount < totalCount - 6:
                    return play

            # Uncomment for offensive statistics
            # if play.offense == team and play.isInterception == 1 or play.isFumble == 1:
                # if playCount > 6 and playCount < totalCount - 6:
                    # return play
        
        return None
    

