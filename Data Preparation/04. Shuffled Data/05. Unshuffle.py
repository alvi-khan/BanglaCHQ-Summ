import pandas as pd
import os

questions = "./01. JSONs/"
annotations = "./05. Cleaned JSONs/"

for file in os.listdir(annotations):
    if not file.endswith('.json'):
        continue
    
    original = pd.read_json(questions + file)
    annotated = pd.read_json(annotations + file)
    original['summary'] = annotated['Summary']
    original = original.sort_values('indices')
    original.to_json(f"../split/{file}", orient='records')
