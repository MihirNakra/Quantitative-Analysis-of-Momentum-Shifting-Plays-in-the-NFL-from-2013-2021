
# Helper class to store relevant play information
class Play:
    
    def __init__(self, gameId, quarter, minute, second, offense, defense, yards, result, isTouchdown, isInterception, isFumble, order=None):
        self.order = order
        self.gameId = gameId
        self.quarter = quarter
        self.minute = minute
        self.second = second
        self.offense = offense
        self.defense = defense
        self.yards = yards
        self.result = result
        self.isTouchdown = isTouchdown
        self.isInterception = isInterception
        self.isFumble = isFumble


    def __str__(self):
        return f"{self.gameId}, {self.quarter} quarter, {self.minute}:{self.second}"

    # Goes through all given plays and puts them in order
    @staticmethod
    def organizePlays(plays):
        quarter = 1
        minute = 15
        second = 0
        orderedPlays = []


        while quarter <= 5:
            for play in plays:
                if play.minute == str(minute) and play.second == str(second) and play.quarter == str(quarter):
                    orderedPlays.append(play)
            
            second -= 1
            if second < 0:
                second = 59
                minute -= 1
            if minute < 0:
                minute = 15
                quarter += 1
            
        return orderedPlays