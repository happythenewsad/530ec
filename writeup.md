Homework 10 Writeup
===================

by Peter Kong
-------------



Instructions
-------------

- To evaluate a prediction file:

```
$ python3 evaluate.py --goldfile data/en-val.txt --predfile val_y_ner_pos_kr_rbf_pred.txt
```

- To generate a prediction file:
```
$ jupyter notebook main.ipynb
```

You can configure models and features within the notebook.

- To run unit tests:
```
$ python3 test_runner.py
```



Discovery and feature extraction
------------------------------------

We first sought to replicate the given baseline and found that its Pearson test score of 0.7322 was higher than the score published in the homework assignment. We attribute this to implementation differences. For example, we identified 19850 unique words in the training corpus, and thus used 19850-vectors during cosine similarity computation. The assignment writers may have used a smaller number.

Our first enhancement was using a stemmer. We found that the Porter stemmer improved the baseline cosine similarity model, for a score of 0.732.

Given the sucess of the cosine similarity feature, we retained it in all future experiments.

We extracted two additional groups of features - Part of Speech features and Named Entity features. We used Spacy libraries to generate these features.

Given our rather small training corpus, we elected to train our POS and NER taggers on an external corpus: the 'en_core_web_sm' corpus. This corpus contains transcripted telephone conversations, blog text, and news wires (link: https://spacy.io/models/en#en_core_web_sm). 'Core Web' does not come from the same theoretical or actual distribution as this assignment's training and test data. However, given the diversity of it's sources and the scope of this project, we are not overly worried about 'Core Web's content bias.

Through manual inspection of the data, we identified 6 pertinent POS tags and 15 entity tags to track:

![](features.png)

For each tag, we computed the absolute difference of tag count between passage 1 and passage 2 for every row of data. For example, if our tagger identified 5 LOCATIONs in passage 1 but only 4 in passage two, it's normalized aboslute difference score would be |5-4|/(5+4) = 1/9.



Model selection
------------------

Holding the features in section 1 constant, we found that our two best additional models were Kernel Ridge Regression and Random Forest Regression. 

Results
-----------

![](error_analysis.png)

KRR achieved the best overal Pearson score of 0.7409 after moving from a linear kernel to a Radial Basis Function kernel and tweaking regularization parameters. Note that it performed only slightly better than the simple baseline.

RFR did not perform very well. It's best test score was 0.6109.


Analysis
------------

Although the POS and NER features improved performance in our winning KRR model, the cosine similarity score between bag-of-words sentence vectors proved to be quite powerful. This was corroborated by the Random Forest Regressor ranking the cosine feature as the most important out of all features.

This indicates that additional improvements may be uncovered by using a bag of synonyms feature, rather than a naive bag of words feature.

The Kernel Ridge Regression tended to be too optimistic when passage 1 and passage 2 contained shared words.

```
Example:
Passage 1: 'a group of people are nervous about crossing the water'
Passage 2: 'a group of people are on the water'
```

KRR predicted score: 4.047
Gold score:			 2.200

It clearly discounts the fact that the non-shared words can substantially affect the semantics of the two passages.

Conclusion
-----------

Our Kernel Ridge Regressor beat the baseline score, but it was noteworthy how the simple cosine similarity model held its own. There are many other features and models to attempt to improve on these results. A feature that identifies similar or identical sentence structures may be useful. Also, discounting adjectives and adverbs may yield improvement; verbs and nouns seem to carry more semantic weight.




