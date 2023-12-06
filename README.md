# BanglaCHQ-Summ: An Abstractive Summarization Dataset for Medical Queries in Bangla Conversational Speech

This repository contains the data and code of ['BanglaCHQ-Summ: An Abstractive Summarization Dataset for Medical Queries in Bangla Conversational Speech'](https://aclanthology.org/2023.banglalp-1.10/), published in the **Proceedings of the First Workshop on Bangla Language Processing (BLP-2023)**, co-located with **The 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)**.

All of the code and the dataset are being provided under the [CC BY-NC-SA 4.0 License](https://creativecommons.org/licenses/by-nc-sa/4.0/). The code provided can be used to re-create the data preparation process we followed, as well as the training and evaluation of the benchmark models.

The repository is divided into the following sections:

 - [Data Preparation](./Data%20Preparation/): Contains the scripts used to collect, clean and prepare the final dataset. Extensive details are provided in [this README file](./Data%20Preparation/README.md).

 - [Dataset](./Dataset/): Contains the final release of the BanglaCHQ-Summ dataset.

- [Scripts](./Scripts/): Contains the scripts used for training and evaluating the benchmark models.

- [Graphics](./Graphics/): Contains the scripts used to create the graphs presented in the paper.

The fine-tuned model weights can be found under the [releases section](https://github.com/alvi-khan/BanglaCHQ-Summ/releases).


## Citation

```
@inproceedings{khan-etal-2023-banglachq,
    title     = "{B}angla{CHQ}-Summ: An Abstractive Summarization Dataset for Medical Queries in {B}angla Conversational Speech",
    author    = "Khan, Alvi and Kamal, Fida and Chowdhury, Mohammad Abrar and Ahmed, Tasnim and Laskar, Md Tahmid Rahman and Ahmed, Sabbir",
    editor    = "Alam, Firoj and Kar, Sudipta and Chowdhury, Shammur Absar and Sadeque, Farig and Amin, Ruhul",
    booktitle = "Proceedings of the First Workshop on Bangla Language Processing (BLP-2023)",
    month     = dec,
    year      = "2023",
    address   = "Singapore",
    publisher = "Association for Computational Linguistics",
    url       = "https://aclanthology.org/2023.banglalp-1.10",
    doi       = "10.18653/v1/2023.banglalp-1.10",
    pages     = "85--93",
    abstract  = "Online health consultation is steadily gaining popularity as a platform for patients to discuss their medical health inquiries, known as Consumer Health Questions (CHQs). The emergence of the COVID-19 pandemic has also led to a surge in the use of such platforms, creating a significant burden for the limited number of healthcare professionals attempting to respond to the influx of questions. Abstractive text summarization is a promising solution to this challenge, since shortening CHQs to only the information essential to answering them reduces the amount of time spent parsing unnecessary information. The summarization process can also serve as an intermediate step towards the eventual development of an automated medical question-answering system. This paper presents {`}BanglaCHQ-Summ{'}, the first CHQ summarization dataset for the Bangla language, consisting of 2,350 question-summary pairs. It is benchmarked on state-of-the-art Bangla and multilingual text generation models, with the best-performing model, BanglaT5, achieving a ROUGE-L score of 48.35{\%}. In addition, we address the limitations of existing automatic metrics for summarization by conducting a human evaluation. The dataset and all relevant code used in this work have been made publicly available.",
}
```