import pandas as pd
import os


df = pd.DataFrame()

for file in os.listdir():
    if not file.endswith('.csv'):
        continue
    
    df = pd.concat([df, pd.read_csv(file)]).reindex()


assert len(df[df.isnull().any(axis=1)]) == 0, "ERROR: Empty Values"
df.to_json('out.json', orient='records')
