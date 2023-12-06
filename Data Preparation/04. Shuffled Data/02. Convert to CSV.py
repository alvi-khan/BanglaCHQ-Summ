import pandas as pd
import os

directory = r"./01. JSONs/"
files = [x for x in os.listdir(directory) if x.endswith('.json')]

for file in files:
    df = pd.read_json(os.path.join(directory, file), encoding='utf-8')
    df = df.drop(['id', 'indices'], axis=1)
    df['summary'] = ""
    df.to_csv(f"./02. CSVs/{file[:-5]}.csv", encoding='utf-8', index=False)
