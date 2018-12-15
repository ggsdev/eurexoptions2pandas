import pandas as pd
import datetime
import math
from datetime import date


df = pd.read_csv('my_file.csv', delimiter=',')

df['Bid'].replace(',','.', inplace=True,regex=True)
df['Bid'].replace('-','0', inplace=True,regex=True)
df['Ask'].replace(',','.', inplace=True,regex=True)
df['Ask'].replace('-','0', inplace=True,regex=True)
df['Bid']=df['Bid'].astype(np.float64)
df['Ask']=df['Ask'].astype(np.float64)

df['Settle'].replace(',','.', inplace=True,regex=True)
df2=df[[0]] + '/18'
df['vdatum']=df2
newdate=pd.to_datetime(df['vdatum'], format='%Y/%m/%d')
df['vdatum']=newdate
df['weekday']=df['vdatum'].dt.dayofweek
df['weekday'].replace('0','7', inplace=True,regex=True)
df['weekday']=df['weekday'].astype(np.float64)
df['timedifference']=df['vdatum']-datetime.datetime.now()   
df['timedifference']=df['timedifference'].dt.days
df['timedifference']=df['timedifference']+4-df['weekday']
