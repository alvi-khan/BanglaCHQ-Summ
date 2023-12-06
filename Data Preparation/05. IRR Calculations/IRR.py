import pandas as pd
from rouge import Rouge
from evaluate import load
from statistics import mean
import os

bertscore = load("bertscore")
DATA_PATH = "../split/"
rouge = Rouge()


def get_rouge_score(summary1, summary2):
    scores = rouge.get_scores(summary1, summary2, avg=True, ignore_empty=True)
    return scores['rouge-l']['f']


def get_bert_score(predictions, references):
    scores = bertscore.compute(
        predictions=predictions.to_list(),
        references=references.to_list(),
        model_type="csebuetnlp/banglabert",
        num_layers=12,
        batch_size=4
    )
    return mean([round(v, 4) for v in scores["f1"]])


data = []

for file in os.listdir(DATA_PATH):
    if not file.endswith(".json"):
        continue
    data.append(pd.read_json(f"{DATA_PATH}/{file}")[-30:]['summary'])

reference = data[0]
hypotheses = data[1:]

rouge_scores = [get_rouge_score(reference, hypothesis) for hypothesis in hypotheses]
bert_scores = [get_bert_score(hypothesis, reference) for hypothesis in hypotheses]

avg_rouge_score = sum(rouge_scores) / len(rouge_scores)
avg_bert_score = sum(bert_scores) / len(bert_scores)

print(f"Average Rouge-L Score: {avg_rouge_score}")
print(f"Average BERT-Score (F1): {avg_bert_score}")
