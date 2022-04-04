import pandas as pd
import numpy as np
import math
import datetime

df = pd.read_csv("country_vaccination_stats.csv")

countries = df["country"].unique()

min_daily_vaccinations = {}

for i in countries:
    min_daily_vaccinations[i] = df.loc[df["country"]==i]["daily_vaccinations"].min()

df.loc[df['daily_vaccinations'].isnull(),'value_is_NaN'] = 'Yes'
df.loc[df['daily_vaccinations'].notnull(), 'value_is_NaN'] = 'No'

for i,row in df.iterrows():
    if row[4] == "Yes":
        if math.isnan(min_daily_vaccinations.get(row[0])) == True:
            df.at[i,'daily_vaccinations'] = 0
        else:
            df.at[i,'daily_vaccinations'] = min_daily_vaccinations.get(row[0])
