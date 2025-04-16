import pandas as pd

file_path = 'trainTest.csv'

df = pd.read_csv(file_path)

print(df['DAY_TYPE'].unique())

from datetime import timedelta

import holidays

portugalHolidays= holidays.country_holidays('PT',subdiv='13') # Don't forget that this data is only based on the ciry Porto (13) in portugal and that is why we used its holidays specifically

portugalHolidays

df['datetime'] = pd.to_datetime(df['TIMESTAMP'], unit='s')

def modifyDayType(r):
    if r['datetime'] in portugalHolidays:portugalHolidays
        r['dayTypeMap'] = 'Holiday'
    elif (r['datetime'] + timedelta(days=1)) in portugalHolidays:
        r['dayTypeMap'] = 'Before_Holiday'
    
    return r 


df = df.apply(modifyDayType)
print(df['datetime'].unique())