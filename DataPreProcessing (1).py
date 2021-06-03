import numpy as np
import pandas as pd

fileName = 'india_thiruvananthapuram_plammoodu_LiveData'
df = pd.read_csv(fileName+'.csv', parse_dates=['Date'])
df.set_index('Date',inplace=True)


df1 = df.interpolate(method="time")

df2 = df1.fillna(method="bfill")

df2.to_csv(fileName+'_preProcessed.csv')




