# Dataset

The dataset is being provided in the form of separate training, validation and test sets to allow our experiments to be reproduced without the additional noise caused by mismatched data shuffling.

Each file consists of samples with 4 values each:
- `ID`, referring to the ID of the question from the website,
- `Question`, which is the question asked by the patient,
- `Summary`, the human-annotated summary
- `Indices`, referring to the index location of the entry in the unshuffled dataset.