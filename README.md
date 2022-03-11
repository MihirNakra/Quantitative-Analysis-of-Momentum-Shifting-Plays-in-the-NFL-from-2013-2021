# Quantitative Analysis of Momentum Shifting Plays in the NFL from 2013 to 2021

by Parth Wokhlu and Mihir Nakra 

Parth Wokhlu: parth.wokhlu.843@gmail.com

Mihir Nakra: nakramihir@gmail.com

# I. Introduction/Purpose
The NFL is the modern-day dramatic theater. Families across America huddle together every Sunday to watch their favorite (and least favorite) teams lock into a suspenseful matchup of brain and brawn. Due to football being as much of a mental game as it is a physical one, the idea of “momentum” has gripped plenty of sports analysts, journalists, and fans. Momentum is the (supposed) mental phenomena where an athlete has increased confidence in their abilities and team after a recent success, and thus performs better. After noticing strange inconsistencies in the theory of momentum’s existence, we decided to look at the numbers in order to reveal the truth. 

# II. Methodology
All the syntax for this project is open-sourced. All files referenced in this write-up are stored above. Please feel free to look through if interested.

## Data Collection
Our first step in data collection was to find where we could pull raw data of NFL games from. Fortunately, the [NFLSavant](http://www.nflsavant.com/) had compiled CSV files of every play from every regular season game from the 2013 to 2021 season. Once we had all the raw data, we needed to process and present it in a way that was useful to us. To do that, we parsed through every play and placed it in a dictionary where it was matched to the game it occurred in. Then, we went through every play in each game and placed it in chronological order. Once we had all the plays ordered and matched to their particular game ID, we saved all that data in a sqlite3 database (‘database.db’). The ‘organize_data.py’ and ‘populate_games.py’ files performed the aforementioned actions to sort through the numbers. 

## Data Analysis
Now that we had all of our data saved in the way we needed it, it was time to analyze it. In order to do so, we first needed to clarify what we were looking for. We defined a momentum-shifting play as any forced turnover that wasn’t in the first or last 6 plays of the game. This was because interceptions/fumbles are often very surprising and are the most commonly mentioned plays when people say “the momentum has shifted.” It couldn’t be within the first or last 6 plays because we then wouldn’t have enough data in the game to look at the change in performance caused by the momentum. 

Then, we parsed through each game and located the first interception or fumble that occurred in each game. Games that did not contain either type of turnover were excluded from this study, as they didn’t have any plays we deemed as a momentum-shifting play. Next, we calculated the average yards per play and average completion percentage of the offense before and after the turnover in each game we identified with one. In order to further verify our study, we aimed to test the positive and negative sides of momentum, so we collected data on the offensive performances of both the team that recovered the turnover and the team that turned the ball over. After compiling all that data, we saved it into CSV files for future analysis. The ‘analyze.py’ file was used to do all that.

## Limitations/Flaws
With any study, there’s going to be a couple of limitations.

1. If a turnover occurred at the very start or very end of the game, then the offensive stats on the before v.s. after analysis could be skewed, as there would be a very small sample size to work off of. To correct this, we didn’t include turnovers that happened within the first or last 6 offensive plays. That way, there would be adequate offensive statistics before and after the turnover to analyze.

2. Some could argue that teams may choose not to play better after a momentum-shifting play as the play (such as a game-ending interception) could have won them the game. However, due to the 6-play restriction, any game ending turnover, where the team that got the turnover just kneels the game away, wouldn’t show up in the data.

3. Another potential limitation is that we only considered two offensive statistics in determining an offense’s success, which were yards per play (YPP) and completion percentage (CP). However, YPP and CP are universal markers of an efficient offense that encompass other statistics, and regardless of other numbers, these two signify offensive success and failure effectively. Moreover, they both were extremely consistent with the other’s findings (both showed no average change). 

4. We only considered fumbles or interceptions as momentum shifting plays, and while this may not include other types of momentum shifting plays, this was a deliberate move. Since in football the defense and offense are two completely separate units, if momentum truly existed, the mental stimulus caused by defensive success should theoretically translate into offensive success.

# III. Results

After collecting the data on two different offensive statistics (Yards per Play (YPP) and Completion Percentage (CP)) before and after a team had a momentum-shifting play on the defense, we were able to analyze it in an Excel file in a couple of ways.

First, we calculated the average change in these metrics throughout all 2000+ games that had a turnover in the past decade. On average, after a team got a turnover on defense, their offense’s YPP decreased by 0.133 yards and their CP decreased by 0.011%. On the flip side, after a team threw an interception/fumbled the ball, their offense’s YPP increased by 0.001 yards and their CP increased by 0.001%.

The changes in both statistics on both sides of the ball are negligible, showing that the impact of an interception/fumble recovery by a team, on average, will not increase the performance of offensive players on that team, nor decrease the performance of the offensive players on the other team. 

Due to an increasingly pass-heavy league, we wanted to see if there was any change in these statistics over time. 

For the team whose defense recovered the turnover:



For the team whose offense threw the turnover:


In both scenarios, there doesn’t seem to be any trend over the years in terms of the impact of a momentum-shifting play.

# IV. Conclusion and Implications 
Considering that there was no significant performance increase or decrease by any team regardless of if they got a turnover or turned the ball over, the idea of momentum seems to be just that, an idea. There’s a couple of reasons this may be the case. First, unlike many other sports, in football, the defense and offense operate separately, so there is a larger disconnect between the halves of a team. Second, players will almost always try their hardest. Whether they want to retain a lead, make a comeback, or want to get the bonus promised in their contract, no matter how well the game is going for them, they will always have an incentive to keep their performance elite. Third, if momentum truly exists, then it’s constantly shifting. If a team throws an interception and then a 60-yard pass its next drive, who has the momentum now? In reality, according to this data, momentum in the NFL just seems to be a very arbitrary classification made up to assign some sort of reasoning to otherwise random events. 
