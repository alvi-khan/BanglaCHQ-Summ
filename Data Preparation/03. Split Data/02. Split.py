import pandas as pd

df = pd.read_json('../data.json')

common_data = df[:30]
df = df[30:]

for i in range(5):
    split = df[i * 500 : (i + 1) * 500]
    split = split[30:]
    split = pd.concat([split, common_data])
    split.to_json(f"../split/{(i + 1) * 500}.json", orient='records')
