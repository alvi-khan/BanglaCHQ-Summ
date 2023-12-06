# Scripts

These are the scripts used to train and evaluate the benchmark models.

For evaluation metrics, the ROUGE-L score and the BERTScore metrics were used.

We have used a slightly modified version of the ROUGE score implementation (refer to [`rouge.py`](rouge.py) and [`rouge_score.py`](rouge_score.py)), which splits sentences based on `।` instead of `.`.

The BERTScore implementation is based on the 12th layer of the BanglaBERT model.