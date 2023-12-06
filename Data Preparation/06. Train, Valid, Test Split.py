import pandas as pd
from sklearn.model_selection import train_test_split

PATH = "../split/"

df = pd.read_json(f"{PATH}/500.json")
df = df[:-30]
df = pd.concat([df, pd.read_json(f"{PATH}/1000.json")])
df = df[:-30]
df = pd.concat([df, pd.read_json(f"{PATH}/1500.json")])
df = df[:-30]
df = pd.concat([df, pd.read_json(f"{PATH}/2000.json")])
df = df[:-30]
df = pd.concat([df, pd.read_json(f"{PATH}/2500.json")])
df = df[:-30]

train, valid = train_test_split(df, test_size=0.2)
valid, test = train_test_split(valid, test_size=0.5)

train.to_csv('train.csv', index=False)
valid.to_csv('valid.csv', index=False)
test.to_csv('test.csv', index=False)
