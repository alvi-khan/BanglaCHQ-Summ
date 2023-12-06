import re
import os
import json
from tqdm import tqdm
import string


def fix_encoding(data):
    text = re.sub(r'\\u0985\\u09be', r'\\u0986', data)
    text = re.sub("অা", "আ", text)

    text = re.sub('“', '"', text)
    text = re.sub(r'\\u201c', r'\\u0022', text)

    text = re.sub('”', '"', text)
    text = re.sub(r'\\u201d', r'\\u0022', text)

    text = re.sub("‘", "'", text)
    text = re.sub(r'\\u2018', r'\\u0027', text)

    text = re.sub("’", "'", text)
    text = re.sub(r'\\u2019', r'\\u0027', text)

    text = re.sub("۔", ".", text)
    text = re.sub(r'\\u06d4', r'\\u002e', text)

    return text


def fix_punctuation_spacing(summary):
    summary = re.sub("([" + re.escape(punctuation) + "])", r" \1 ", summary)
    summary = re.sub(u"\u09f7", u" \u09f7 ", summary)
    summary = re.sub(u"\u0964", u" \u0964 ", summary)
    summary = re.sub('\s{2,}', ' ', summary)
    return summary


directory = './04. Annotated JSONs/'
punctuation = string.punctuation

for filename in tqdm(os.listdir(directory)):
    if not filename.endswith('.json'):
        continue

    f = os.path.join(directory, filename)
    if not os.path.isfile(f):
        continue

    data = None
    with open(f, encoding='utf-8') as file:
        data = file.read()

    if data is None:
        continue

    data = fix_encoding(data)

    df = json.loads(data)
    df = [{"Question": item['Question'], "Summary": fix_punctuation_spacing(item['Summary'])} for item in df]

    f = os.path.join('./05. Cleaned JSONs', filename)
    with open(f, 'w', encoding='utf-8') as file:
        file.write(json.dumps(df))
