# Data load anad clean
import pandas as pd
import numpy as np

raw = pd.read_excel('car-counts.xlsx')
raw['imaging_ts']=pd.to_datetime(raw['imaging_ts'])
raw['day']=raw['imaging_ts'].dt.dayofweek
grouped = raw.groupby(['imaging_ts','day'], as_index=False)['objects detected'].sum()
grouped = grouped.merge(raw[['cloud_score','imaging_ts']], 
                        left_on = 'imaging_ts', right_on = 'imaging_ts')
grouped = grouped.groupby(['imaging_ts','day','objects detected'], as_index=False)['cloud_score'].mean()
grouped['sqcloud']=np.power(grouped['cloud_score'],2)
# labelling days of the week
grouped['month']=grouped['imaging_ts'].dt.month
grouped['year']=grouped['imaging_ts'].dt.year
latest=grouped.loc[grouped['year']==2016]