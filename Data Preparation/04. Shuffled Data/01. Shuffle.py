import os
import pandas as pd

directory = r"../split"
files = [x for x in os.listdir(directory) if x.endswith('.json')]


for file in files:
    df = pd.read_json(os.path.join(directory, file))
    df['indices'] = list(range(len(df)))
    df = df.sample(frac=1).reset_index(drop=True)
    df.to_json(f"./01. JSONs/{file}", orient='records')
