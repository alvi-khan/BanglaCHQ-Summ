# Data Preparation

The dataset was prepared in a series of steps using several scripts, as outlined below:

## Step 01: Scraping the data from the website

[`01. Scrape Data from Website.py`](01.%20Scrape%20Data%20from%20Website.py)

Each question and the corresponding answers were stored in a separate file in a `data` folder. The filenames correspond to the IDs of the questions on the website. If you are following these instructions, please make sure to keep a backup of the downloaded files since the next steps modify the files.

## Step 2: Cleanup

[`01. Combine.py`](02.%20Cleanup/01.%20Combine.py)

Combines all the files into a single JSON, `data.json`. This file is the one we work with in the following steps.

[`02. Remove Duplicates.py`](02.%20Cleanup/02.%20Remove%20Duplicates.py)

Removes duplicate questions, retaining only one copy.
- The step deletes the files for the duplicate questions.
- A duplicate refers to exact matches. Very similar questions that were most likely spammed by the same author are not removed.
- Which duplicate to retain is determined based on which one has answers to the question.
- In cases where one or more duplicates all have answers, they are not deleted. These must be reviewed manually.
- Duplicate answers under the same question are removed.

[`03. Clean (Manual).py`](02.%20Cleanup/03.%20Clean%20(Manual).py)

Cleans the data. This process involves manual inspections.
- Spam questions are identified using a [gibberish detector](https://github.com/rrenaud/Gibberish-Detector). These are displayed on the terminal and must be manually approved before they are deleted. A copy of the source code for the gibberish detector is included.
- Emails, numbers (5 digits or more) and links in the question and each of the answers are removed using regex. Any changes must be approved before they are saved.

[`04. Find Names.py`](02.%20Cleanup/04.%20Find%20Names.py)

Named were identified using a [general Bangla NER model](https://pypi.org/project/bnlp-toolkit). A copy of the model is included.
- Each detection requires manual approval.
- The model frequently made erroneous detections on specific nouns. A list of such nouns was created over time and included in the script so such detections could be skipped.
- The IDs of the samples with names detected in them were stored. These names were then manually removed.

[`05. Clean (Auto).py`](02.%20Cleanup/05.%20Clean%20(Auto).py)

Fixes encoding, punctuation and spacing issues.

[`01. Combine.py`](02.%20Cleanup/01.%20Combine.py)

The cleaned files are combined back into a single JSON file, `data.json`.

## Step 3: Split Data

[`01. Remove Short Data.py`](03.%20Split%20Data/01.%20Remove%20Short%20Data.py)

Removes any samples that contain non-Bangla characters or are shorter than 225 characters.

[`02. Split.py`](03.%20Split%20Data/02.%20Split.py)

The data was split into groups of 500 samples. The first 30 samples in each group were replaced with the first 30 samples of the dataset, which is considered the control group.

## Step 4: Shuffled Data

[`01. Shuffle.py`](04.%20Shuffled%20Data/01.%20Shuffle.py)

Shuffles the data.

[`02. Convert to CSV.py`](04.%20Shuffled%20Data/02.%20Convert%20to%20CSV.py)

Converts the JSON files to CSV files. These CSV files were uploaded to Google Sheets and shared with the annotators. For ease of annotation, each CSV was also manually separated into 5 separate sheets.

[`03. Combine Annotations.py`](04.%20Shuffled%20Data/03.%20Combine%20Annotations.py)

Each of the sheets was downloaded separately after annotations were complete. This script combines the sheets back into JSON files.

A portion of this work was done manually to make sure that groups of 5 sheets were combined into the correct JSON file.

[`04. Clean.py`](04.%20Shuffled%20Data/04.%20Clean.py)

Cleans the annotated summaries. Spaces are added around punctuation, encoding issues are fixed, and multiple consecutive spaces are removed.

[`05. Unshuffle.py`](04.%20Shuffled%20Data/05.%20Unshuffle.py)

The questions are replaced with the questions from the original shuffled files. This is done to make sure that any modifications made to the questions by mistake during the annotation process are not retained in the final data. The data is then unshuffled.

## Step 5: IRR Calculations

[`IRR.py`](05.%20IRR%20Calculations/IRR.py)

The common data from each set of 500 samples (the first 30 samples) were used to calculate the IRR. There are two metrics we considered for IRR, ROUGE-L Score and BERTScore. Both of these use a customized implementation for Bangla, as described in [this README file](../Scripts/README.md). Both scores are averaged across the 5 sets.

## Step 6: Split the data into train, valid and test files

[`06. Train, Valid, Test Split.py`](06.%20Train,%20Valid,%20Test%20Split.py)

Splits the data into train, validation and test sets. It also removes the common data (the first 30 samples of each set). The common data was left out of the final dataset.