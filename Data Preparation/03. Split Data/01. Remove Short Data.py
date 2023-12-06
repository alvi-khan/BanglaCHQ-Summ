import pandas as pd
import string

min_length = 225

df = pd.read_json('../data.json')

# remove answers and date columns
df = df.drop(['answers', 'date', 'tag'], axis=1)

# remove non-bangla text
alphabets = list(string.ascii_lowercase) + list(string.ascii_uppercase)
ids = [row['id'] for i, row in df.iterrows() if not any(alphabet in row['question'] for alphabet in alphabets)]
df = df[(df['id'].isin(ids))]

# remove short questions and questions with no tags
df = df[(df['question'].str.len() > min_length)]

# remove duplicate questions except first ones
df = df.drop_duplicates(subset=["question"], keep="first")
df.to_json('../data.json', orient='records')
