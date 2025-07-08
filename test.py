# Import package 
import swehockey.swehockey_scraper as swe
import numpy as np
import pandas as pd

# Read in needed schedule-ids
df_swehockey = pd.read_csv("https://raw.githubusercontent.com/msjoelin/swehockey_scraper/master/data/scheduleid.csv", 
                          dtype=str)
df_swehockey = pd.read_csv("./scheduleid.csv",
                          dtype=str)

print(df_swehockey)


# get games for some schedule ids
games = swe.getGames(df_swehockey['schedule_id'])
#print(df_swehockey['schedule_id'])
#games = swe.getGames("15986")
print(games)

