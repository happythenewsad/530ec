Peter Kong - Homework 10 Writeup
=========================

Instructions: 

$ python3 evaluate.py --goldfile data/en-val.txt --predfile val_y_ner_pos_kr_rbf_pred.txt

You can use one of the bundled prediction files, or generate your own by configuring and executing main.ipynb.



I. Discovery and feature extraction
----------------------

We first sought to replicate the given baseline, and found that its Pearson score of 0.711 was higher than the score published in the homework assignment. We attribute this to implementation differences. For example, we identified 19850 unique words in the training corpus, and thus used 19850-vectors during cosine similarity computation. The assignment writers may have used a smaller number.

Our first enhancement was using a stemmer. We found that the Porter stemmer improved the baseline cosine similarity model, for a score of 0.732.

Given the sucess of the cosine similarity feature, we retained it in all future experiments.

We extracted two additional groups of features - Part of Speech features and Named Entity features. We used Spacy libraries to generate these features.

Given our rather small training corpus, we elected to train our POS and NER taggers on an external corpus: the 'en_core_web_sm' corpus. This corpus contains transcripted telephone conversations, blog text, and news wires (link: https://spacy.io/models/en#en_core_web_sm). 'Core Web' does not come from the same theoretical or actual distribution as this assignment's training and test data. However, given the diversity of it's source and the scope of this project, we are not overly worried about 'Core Web's content bias.

Through manual inspection of the data, we identified 6 pertinent POS tags and 15 entity tags to track:

[image]

For each tag, we computed the absolute difference of tag count between passage 1 and passage 2 for every row of data. For example, if our tagger identified  5 locations in passage 1 but only 4 in passage two, it's normalized aboslute difference score would be |5-4|/(5+4) = 1/9.



2. Model selection
------------------
Holding the features in section 1 constant, we found that our two best additional models were Kernel Ridge Regression and Random Forest Regression. 

KRR achieved the best overal Pearson score of 0.7409 after using moving from a linear to a Radial Basis Function kernel and tweaking regularization parameters. Amazingly, it did only slightly bett


3. More feature extraction and tuning
-------------------------------------
In order to improve f1, we re-examined our features. Since our feature
count had grown to almost 200k, we worried that the
start-of-sentence and end-of-sentence features were getting lost
in the noise. We created a tunable parameter mu to amplify these two
to features:
Value of mu : f1 score
----------------------
x*1: 65.75
x*5: 65.83 (chosen parameter)
x*10: 65.49
We also revisited our features. We broaded the neighboring word window
which yielded significant improvements:
Window width : f1 score
-----------------------
3 (baseline): 65.83
5: 65.75 (chosen parameter)
7: 67.34
11: 67.11
Adding additional context of surrounding words to a model increases f1
score, to a point. If the window is larger than about
6, recall starts to fall, bringing the f1 score down with it.




4. Dimensionality reduction
----------------------------
After the above tests, we trained on both esp.train and esp.testa,
yielding our best f1 score of 71.46
Because our feature count was on the order of our row count, we
attempted dimensionality reduction via SVD:
SVD n_components : f1 score
---------------------------
20: 38
200: 56.55
400: 57.64
800: 59.52
3200: 62.32
The results continue to increase with n, indicating that there is
likely a good score 3200 < x < |features|
Unfortunately, the n=3200 run took over 70 minutes, so further
investigation was not feasible and SVD was not used in the final
result.



5. Notes and observations
---------------------------
According to (Ratinov, Roth, CONLLL 09), it is highly likely that
incorporating a gazeteer would dramatically improve the model.
Entities like 'Espana' that appear multiple times within the corpora
could be tagged as entities with near 100% precision (excluding
polysemous entities and entity compositions like ;Reino de España',
aka 'The Kingdom of Spain.'


pred: 4.046746672214708

a group of people are nervous about crossing the water .	a group of people are on the water .	2.200000
